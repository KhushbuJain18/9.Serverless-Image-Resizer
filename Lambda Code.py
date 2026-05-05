import boto3
from PIL import Image
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    download_path = f"/tmp/{key}"
    upload_path = f"/tmp/resized-{key}"

    # Download image from S3
    s3.download_file(bucket, key, download_path)

    # Resize image
    with Image.open(download_path) as img:
        img = img.resize((300, 300))
        img.save(upload_path)

    # Upload to output bucket
    output_bucket = "image-resizer-output-12345"

    s3.upload_file(upload_path, output_bucket, f"resized-{key}")

    return {
        'statusCode': 200,
        'body': 'Image resized successfully'
    }
