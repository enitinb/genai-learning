'''
This is a python module to interact with amazon bedrock LLM models. Currently it supports titan, claude and jurrasic
Usage : 
    1. Import module using "import amz_brck_llm_cfg" 
    2. call the function using "amz_brck_llm_cfg.interactWithLLM(prompt,llm_type,bedrock_client)" 

    
Param details : 
    prompt : Prompt to pass 
    llm_type : LLM type value to use, currently supports titan, claude and jurrasic
    bedrock_client : boto3 client, example : boto3.client('bedrock' , region, endpoint_url = amazon_bedrock_endpoint_url)

This module uses llm_config.ini file with details as below 

    [titan]
    modelId = amazon.titan-tg1-large
    accept = application/json
    contentType = application/json
    body_config = {"inputText": "{prompt}", "textGenerationConfig": {"maxTokenCount":512,"stopSequences":[],"temperature":0,"topP":0.9}}

''' 

import json
import configparser

config = configparser.ConfigParser()
config.read('llm_config.ini')

def interactWithLLM(prompt,type,bedrock_client):

    print("**THE LLM TYPE IS -->" + type)

    modelId = config[type]['modelId']
    accept = config[type]['accept']
    contentType = config[type]['contentType']
    
    body_config = config[type]['body_config']
    body_config = body_config.replace("{prompt}",prompt)
    print("body_config---" + body_config)

    body = json.dumps(json.loads(body_config,strict=False))
    
    response = bedrock_client.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )

    print("response---" + str(response))
    response_body = json.loads(response.get("body").read())
    

    if type == 'titan':
        response_text_titan = response_body.get("results")[0].get("outputText")
        return response_text_titan
    elif type == 'claude':
        response_text_claude = response_body.get('completion')
        return response_text_claude
    elif type == 'jurassic':
        response_text_jurassic = response_body.get('completions')[0].get("data").get("text")
        return response_text_jurassic