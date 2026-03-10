import requests
import mysql.connector
from datetime import datetime

# Database connection configuration
DB_CONFIG = {
    'host': 'ds2002.cgls84scuy1e.us-east-1.rds.amazonaws.com',
    'user': 'ds2002',
    'password': 'Xf3$fa57CwD!',
    'database': 'iss'
}

def get_db_connection():
    """Establish and return a database connection."""
    return mysql.connector.connect(**DB_CONFIG)

def register_reporter(reporter_id, reporter_name):
    """Register the reporter in the database if they don't already exist."""
    db = None
    cursor = None
    try:
        db = get_db_connection()
        cursor = db.cursor()
        
        # Check if the reporter already exists
        cursor.execute("SELECT * FROM reporters WHERE reporter_id = %s", (reporter_id,))
        result = cursor.fetchone()
        
        if not result:
            # Insert new reporter using parameterized query
            insert_query = "INSERT INTO reporters (reporter_id, reporter_name) VALUES (%s, %s)"
            cursor.execute(insert_query, (reporter_id, reporter_name))
            db.commit()
            print(f"Registered new reporter: {reporter_id}")
        else:
            print(f"Reporter {reporter_id} already registered.")
            
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        if cursor: cursor.close()
        if db: db.close()

def extract():
    """Fetch the current ISS location from the open-notify API."""
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def load(data, reporter_id):
    """Parse the API data and insert it into the locations table."""
    if not data or data.get('message') != 'success':
        print("Invalid data received. Skipping load.")
        return

    db = None
    cursor = None
    try:
        # Parse data
        message = data['message']
        lat = float(data['iss_position']['latitude'])
        lon = float(data['iss_position']['longitude'])
        
        # Convert UNIX timestamp to YYYY-MM-DD HH:MM:SS
        raw_timestamp = data['timestamp']
        formatted_time = datetime.fromtimestamp(raw_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Connect and insert
        db = get_db_connection()
        cursor = db.cursor()
        
        insert_query = """
            INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (message, lat, lon, formatted_time, reporter_id))
        db.commit()
        print(f"Inserted location: Lat {lat}, Lon {lon} at {formatted_time}")
        
    except mysql.connector.Error as err:
        print(f"Database Error during load: {err}")
    finally:
        if cursor: cursor.close()
        if db: db.close()

def main():
    # Use your computing ID
    reporter_id = "sub5gd"
    reporter_name = "DS2002 Student" 
    
    # 1. Register yourself
    register_reporter(reporter_id, reporter_name)
    
    # 2. Extract Data
    iss_data = extract()
    
    # 3. Load Data
    load(iss_data, reporter_id)

if __name__ == "__main__":
    main()