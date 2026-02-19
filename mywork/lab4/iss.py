#!/usr/bin/python3
import requests
import pandas as pd
import logging
import sys
import os
import time

def setup_logger():
    """Initializes a logger that outputs to both console and a file."""
    logger = logging.getLogger("ISS_Tracker")
    logger.setLevel(logging.INFO)
    
    # Create handlers
    c_handler = logging.StreamHandler() # Console
    f_handler = logging.FileHandler('iss_pipeline.log') # File
    
    # Create formatters and add to handlers
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(format)
    f_handler.setFormatter(format)
    
    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    return logger

logger = setup_logger()

def extract():
    """Downloads raw JSON data from the ISS API."""
    url = "http://api.open-notify.org/iss-now.json"
    try:
        logger.info("Extracting data from API...")
        response = requests.get(url)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()
        return data
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        sys.exit(1)

def transform(json_data):
    """Converts JSON into a pandas DataFrame and formats the timestamp."""
    try:
        logger.info("Transforming data...")
        # Flatten the nested 'iss_position'
        flat_data = {
            'timestamp': json_data['timestamp'],
            'latitude': json_data['iss_position']['latitude'],
            'longitude': json_data['iss_position']['longitude']
        }
        df = pd.DataFrame([flat_data])
        
        # Convert UNIX timestamp to YYYY-MM-DD HH:MM:SS
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        
        return df
    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        sys.exit(1)

def load(df, filename):
    """Appends the DataFrame to a CSV file."""
    try:
        logger.info(f"Loading data into {filename}...")
        # If file doesn't exist, write with header. If it does, append without header.
        if not os.path.isfile(filename):
            df.to_csv(filename, index=False)
        else:
            df.to_csv(filename, mode='a', header=False, index=False)
    except Exception as e:
        logger.error(f"Loading failed: {e}")

def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python3 iss.py <output_csv_name>")
        sys.exit(1)
        
    output_file = sys.argv[1]
    
    # Run the ETL pipeline
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data, output_file)
    logger.info("ETL Cycle Complete.")

if __name__ == "__main__":
    main()