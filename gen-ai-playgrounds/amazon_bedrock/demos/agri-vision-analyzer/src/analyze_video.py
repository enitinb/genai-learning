import json
import boto3
import os
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
bedrock = boto3.client("bedrock-runtime", region_name=os.environ.get('REGION', 'us-east-1'))
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def lambda_handler(event, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }

    try:
        body = json.loads(event['body'])
        file_key = body.get("fileKey")
        custom_prompt = body.get("prompt", "").strip()
        
        if not file_key:
            return {'statusCode': 400, 'body': json.dumps({'error': 'Missing fileKey'})}

        bucket_name = os.environ['UPLOAD_BUCKET']

        system_prompt = "You are an expert in video analysis. Analyze the video content and provide insights."
        user_prompt = custom_prompt if custom_prompt else "Analyze this video and provide detailed insights."

        system_list = [{"text": system_prompt}]
        message_list = [{
            "role": "user",
            "content": [
                {"video": {"format": "mp4", "source": {"s3Location": {"uri": f"s3://{bucket_name}/{file_key}"}}}},
                {"text": user_prompt}
            ]
        }]

        inf_params = {"max_new_tokens": 500, "top_p": 0.1, "top_k": 20, "temperature": 0.3}

        native_request = {
            "schemaVersion": "messages-v1",
            "messages": message_list,
            "system": system_list,
            "inferenceConfig": inf_params
        }

        print("Invoking Bedrock Model with Request:", json.dumps(native_request, indent=2))

        response = bedrock.invoke_model(modelId="us.amazon.nova-lite-v1:0", body=json.dumps(native_request))
        response_body = response['body'].read()
        model_response = json.loads(response_body)

        content_text = model_response["output"]["message"]["content"][0].get("text", "No response text found")

        # Save analysis results in DynamoDB
        table.put_item(
            Item={
                "fileKey": file_key,
                "filename": file_key.split("/")[-1],
                "videoUrl": f"https://{bucket_name}.s3.amazonaws.com/{file_key}",
                "analysis": content_text,
                "timestamp": datetime.utcnow().isoformat(),
                "customPromptUsed": bool(custom_prompt),
                "user_prompt" : user_prompt,
                "system_prompt" : system_prompt
            }
        )

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'insights': content_text.strip().split('\\n'), 'raw_response': content_text})
        }

    except Exception as e:
        print("Error:", str(e))
        return {'statusCode': 500, 'headers': headers, 'body': json.dumps({'error': str(e)})}
