import json

import boto3


s3_client = boto3.client("s3")


def lambda_handler(event, context):
    print(str(event))
    bucket = event["detail"]["requestParameters"]["bucketName"]
    print(bucket)
    json_file_name = event["detail"]["requestParameters"]["key"]
    print(json_file_name)
    json_object = s3_client.get_object(Bucket=bucket, Key=json_file_name)
    jsonFileReader = json_object["Body"].read()
    return "Hello from Lambda"
