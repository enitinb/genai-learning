import json
import boto3
import os
import uuid

s3 = boto3.client('s3')
UPLOAD_BUCKET = os.environ['UPLOAD_BUCKET']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        filename = body.get('filename', 'video.mp4')
        content_type = body.get('contentType', 'video/mp4')

        file_key = f"uploads/{uuid.uuid4()}_{filename}"

        # Generate pre-signed URL valid for 15 minutes
        presigned_url = s3.generate_presigned_url(
            'put_object',
            Params={'Bucket': UPLOAD_BUCKET, 'Key': file_key, 'ContentType': content_type},
            ExpiresIn=900
        )

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'presignedUrl': presigned_url, 'fileKey': file_key})
        }
    except Exception as e:
        print("Error:", str(e))
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
