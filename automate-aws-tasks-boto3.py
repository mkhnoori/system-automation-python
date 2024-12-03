import boto3

def upload_to_s3(bucket_name, file_name, object_name=None):
    s3 = boto3.client('s3')
    try:
        if not object_name:
            object_name = file_name
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"{file_name} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

# Example usage
upload_to_s3("my-bucket", "/path/to/file.txt")
