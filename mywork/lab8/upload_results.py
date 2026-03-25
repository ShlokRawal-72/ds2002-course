import os
import glob
import logging
import argparse
import boto3

# Set up logging to print to the console
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def parse_args():
    """
    Parses command line arguments for the input folder and S3 destination.
    """
    parser = argparse.ArgumentParser(description="Upload lab 07 CSV results to S3")
    parser.add_argument("input_folder", help="Path to the folder containing results-*.csv files")
    parser.add_argument("destination", help="S3 bucket and prefix (e.g., ds2002-sub5gd/book-analysis/)")
    return parser.parse_args()

def upload(input_folder, destination):
    """
    Uploads all 'results-*.csv' files from the input folder to the specified S3 destination.
    """
    # Parse the destination string into bucket and prefix components
    parts = destination.strip("/").split("/", 1)
    bucket = parts[0]
    prefix = parts[1] + "/" if len(parts) > 1 else ""

    s3 = boto3.client('s3', region_name='us-east-1')
    
    # Find all CSV files matching the naming convention
    search_pattern = os.path.join(input_folder, "results-*.csv")
    files_to_upload = glob.glob(search_pattern)

    if not files_to_upload:
        logging.warning(f"No files matching 'results-*.csv' found in {input_folder}")
        return False

    success = True
    for file_path in files_to_upload:
        file_name = os.path.basename(file_path)
        s3_key = f"{prefix}{file_name}"
        
        # Wrapped in try/except as per the rubric
        try:
            logging.info(f"Uploading {file_name} to s3://{bucket}/{s3_key}")
            s3.upload_file(file_path, bucket, s3_key)
        except Exception as e:
            logging.error(f"Failed to upload {file_name}. Error: {e}")
            success = False
            
    return success

def main():
    """Main execution function."""
    args = parse_args()
    logging.info("Starting S3 upload process...")
    
    result = upload(args.input_folder, args.destination)
    
    if result:
        logging.info("Success! All files uploaded without errors.")
    else:
        logging.error("Upload process finished, but some errors occurred.")

if __name__ == "__main__":
    main()