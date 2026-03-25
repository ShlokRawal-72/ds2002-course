#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local_file> <bucket_name> <expiration_in_seconds>"
    exit 1
fi

LOCAL_FILE=$1
BUCKET=$2
EXPIRATION=$3

# Extract just the filename from the path
FILENAME=$(basename "$LOCAL_FILE")

echo "Uploading $LOCAL_FILE to s3://$BUCKET/"
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET/"

echo "-----------------------------------"
echo "Generating presigned URL for $FILENAME (expires in $EXPIRATION seconds):"
aws s3 presign "s3://$BUCKET/$FILENAME" --expires-in "$EXPIRATION"