import json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

table_name = os.environ['DYNAMODB_TABLE']
bucket_name = os.environ['UPLOAD_BUCKET']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }
    
    try:
        response = table.scan()
        items = response.get("Items", [])
        
        records = []
        for item in sorted(items, key=lambda x: x["timestamp"], reverse=True):
            # Generate Pre-signed URL for Video Playback
            presigned_url = s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': item["fileKey"]},
                ExpiresIn=3600  # 1 hour expiry
            )

            records.append({
                "videoId": item["fileKey"],
                "filename": item["filename"],
                "videoUrl": presigned_url,
                "analysis": item["analysis"],
                "timestamp": item["timestamp"],
                "customPromptUsed": item.get("customPromptUsed", "No"),
                "user_prompt" : item["user_prompt"],
                "system_prompt" : item["system_prompt"]
            })

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"records": records})
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": str(e)})
        }
