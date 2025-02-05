import json
import boto3
import os
import uuid
from datetime import datetime

# Initialize AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Get environment variables
UPLOAD_BUCKET = os.environ['UPLOAD_BUCKET']
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        filename = body.get('filename', 'video.mp4')
        content_type = body.get('contentType', 'video/mp4')

        # Generate unique file key (new UUID ensures uniqueness)
        file_key = f"uploads/{uuid.uuid4()}_{filename}"

        # Generate pre-signed URL valid for 15 minutes
        presigned_url = s3.generate_presigned_url(
            'put_object',
            Params={'Bucket': UPLOAD_BUCKET, 'Key': file_key, 'ContentType': content_type},
            ExpiresIn=900
        )

        # Store/update video metadata in DynamoDB
        table = dynamodb.Table(DYNAMODB_TABLE)
        video_metadata = {
            "fileKey": file_key,
            "timestamp": datetime.utcnow().isoformat(),
            "filename": filename,
            "status": "uploaded"
        }
        table.put_item(Item=video_metadata)  # Overwrites if exists

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'presignedUrl': presigned_url, 'fileKey': file_key})
        }

    except Exception as e:
        print("Error:", str(e))
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
