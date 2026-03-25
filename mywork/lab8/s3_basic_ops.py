import boto3

def main():
    # Initialize the S3 client
    s3 = boto3.client('s3', region_name='us-east-1')
    
    bucket_name = 'ds2002-sub5gd'
    private_file = 'cloud.jpg'
    public_file = 'another_image.jpg' # Make sure you have a second image downloaded for this

    # 1. Upload a file to S3 and keep it private
    print(f"Uploading {private_file} (Private)...")
    s3.upload_file(private_file, bucket_name, private_file)
    print("Private upload complete.\n")

    # 2. Upload a file to S3 and make it public
    print(f"Uploading {public_file} (Public)...")
    s3.upload_file(
        public_file, 
        bucket_name, 
        public_file, 
        ExtraArgs={'ACL': 'public-read'}
    )
    print("Public upload complete.\n")

    # 3. Generate a presigned URL for the private file
    print("Generating presigned URL for the private file...")
    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': private_file},
        ExpiresIn=300  # Expires in 5 minutes
    )
    
    print("Presigned URL:")
    print(presigned_url)

if __name__ == "__main__":
    main()