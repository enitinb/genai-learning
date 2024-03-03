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

def format_text_claud(text):
    prefix = "Human: " 
    suffix = " Assistant: "
    
    formatted_text = prefix + text + suffix
    return formatted_text

def format_text_llama(text):
    prefix = "[INST] " 
    suffix = " [/INST]"
    
    formatted_text = prefix + text + suffix
    return formatted_text

def interactWithLLM(prompt,type,bedrock_client):
    
    print("**THE LLM TYPE SELECTED IS -->" + type)
    print("\n")
    
    #claude and llama needs to have a specific format for the prompt
    if type == 'claude':
        formatted_prompt_claud = format_text_claud(prompt)
        print("*** Formatted text for claude ***")
        print("\n")
        print(formatted_prompt_claud)
        print("\n")
        prompt = formatted_prompt_claud
    if type == 'llama':
        formatted_text_llama = format_text_llama(prompt)
        print("*** Formatted text for llama ***")
        print("\n")
        print(formatted_text_llama)
        print("\n")
        prompt = formatted_text_llama


    modelId = config[type]['modelId']
    accept = config[type]['accept']
    contentType = config[type]['contentType']
    
    body_config = config[type]['body_config']
    body_config = body_config.replace("{prompt}",prompt)
    print("body_config sending to the model API---" + body_config)
    print("\n")

    body = json.dumps(json.loads(body_config,strict=False))
    
    response = bedrock_client.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )

    print("response from API ---> " + str(response))
    print("\n")
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
    elif type == 'cohere':
        print(response_body)
        response_text_cohere = response_body.get('generations')[0].get("text")
        return response_text_cohere
    elif type == 'llama':
        response_text_llama = response_body.get('generation')
        return response_text_llama