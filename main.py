import os
from zip import zip_directory
from aws import aws_upload

if __name__ == '__main__':

    # The name of the AWS S3 bucket
    bucket_name = 'my-company-backups-it332-capstone'

    # Zip the current working directory
    zip_path = zip_directory()
    print(f'Zipped {zip_path}')

    # Upload the zipped file to AWS S3
    aws_upload(zip_path, bucket_name)

    # Delete the zipped file
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f'{zip_path} was removed.')
