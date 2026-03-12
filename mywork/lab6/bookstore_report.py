import os
from pymongo import MongoClient

# Fetch environment variables set in ~/.bashrc
MONGO_URL = os.getenv("MONGODB_ATLAS_URL")
MONGO_USER = os.getenv("MONGODB_ATLAS_USER")
MONGO_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():
    # Connect to MongoDB Atlas using the credentials
    print("Connecting to MongoDB Atlas...")
    client = MongoClient(MONGO_URL, username=MONGO_USER, password=MONGO_PWD)
    
    # Target the bookstore database and authors collection
    db = client["bookstore"]
    collection = db["authors"]
    
    # Print the report header
    print("\n--- Bookstore Author Report ---")
    
    # 1. Total number of author documents
    total_authors = collection.count_documents({})
    print(f"Total Authors in Inventory: {total_authors}\n")
    
    # 2. List of names and nationalities
    print("Author Details:")
    authors = collection.find({})
    
    for author in authors:
        # Use .get() to avoid errors if a field is missing
        name = author.get("name", "Unknown Name")
        nationality = author.get("nationality", "Unknown Nationality")
        print(f"- {name} ({nationality})")
        
    # Close the connection
    client.close()
    print("\nConnection closed.")

if __name__ == "__main__":
    main()