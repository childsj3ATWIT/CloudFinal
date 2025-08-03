import boto3

def minio():
    print("Connecting to MinIO...")
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin123',
        region_name='us-east-1'
    )

    bucket = 'cloud-storage'
    file_content = b"CloudFinal"
    filename = 'test.txt'

    try:
        s3.create_bucket(Bucket=bucket)
    except s3.exceptions.BucketAlreadyOwnedByYou:
        pass
    except s3.exceptions.BucketAlreadyExists:
        pass

    s3.put_object(Bucket=bucket, Key=filename, Body=file_content)
    obj = s3.get_object(Bucket=bucket, Key=filename)
    data = obj['Body'].read().decode()
    print("MinIO file content:", data)


if __name__ == '__main__':
    minio()
