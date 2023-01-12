import boto3
import os
import botocore
from dotenv import load_dotenv


def aws_upload(file_path, bucket_name):
    # Load environment variables from a .env file
    load_dotenv()

    # Use the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables
    # to create an S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    try:
        s3.create_bucket(Bucket=bucket_name)
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            # create the bucket
            s3.create_bucket(Bucket=bucket_name)
    # Use the S3 client to upload the file
    s3.upload_file(file_path, bucket_name, os.path.basename(file_path))
    print(f'Successfully uploaded {file_path} to {bucket_name}')
