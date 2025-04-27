# list_s3_buckets_and_objects.py

import boto3

def list_s3_buckets_and_count_objects(bucket_name):
    # Create S3 client
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    # List all buckets
    response = s3_client.list_buckets()
    print("Available S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")

    # Count number of objects in the specified bucket
    bucket = s3_resource.Bucket(bucket_name)
    object_count = sum(1 for _ in bucket.objects.all())
    print(f"\nTotal number of objects in bucket '{bucket_name}': {object_count}")

if __name__ == "__main__":
    # Specify your bucket name here
    bucket_name = 'tushar-static-site-bucket-2025'
    list_s3_buckets_and_count_objects(bucket_name)
