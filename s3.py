import boto3
from config import AWS_ACCESS_KEY, AWS_SECRET, S3_BUCKET
import os

def upload_to_s3(file_path):
    # Create S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET
    )

    # Extract file name from path
    file_name = os.path.basename(file_path)

    # Upload file
    s3.upload_file(file_path, S3_BUCKET, file_name)
    print(f"✅ Uploaded {file_name} to S3 bucket '{S3_BUCKET}'")

if __name__ == "__main__":
    # Example usage
    transformed_file = "transformed_stock_data20250814_1457"  # Change to your transformed CSV
    upload_to_s3(transformed_file)
