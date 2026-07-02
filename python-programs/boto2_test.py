import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
print("s3 buckets:")
for bucket in response['Buckets']:
    print(f"Bucket name: {bucket['Name']}")
	