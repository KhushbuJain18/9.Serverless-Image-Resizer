import boto3
import json

s3 = boto3.client('s3')

OUTPUT_BUCKET = "image-output-bucket-demo-12345"

def lambda_handler(event, context):

    # Get uploaded file info
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    copy_source = {
        'Bucket': source_bucket,
        'Key': file_key
    }

    # Copy file to output bucket with resized- name
    s3.copy_object(
        CopySource=copy_source,
        Bucket=OUTPUT_BUCKET,
        Key="resized-" + file_key
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Image stored with resized name successfully")
    }
