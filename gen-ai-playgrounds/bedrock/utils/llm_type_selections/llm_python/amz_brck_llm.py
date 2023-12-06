'''
This is a python module to interact with amazon bedrock LLM models. Currently it supports titan, claude and jurrasic
Usage : 
    1. Import module using "import amz_brck_llm" 
    2. call the function using "amz_brck_llm.interactWithLLM(prompt,llm_type,bedrock_client)" 

    
Param details : 
    prompt : Prompt to pass 
    llm_type : LLM type value to use, currently supports titan, claude and jurrasic
    bedrock_client : boto3 client, example : boto3.client('bedrock' , region, endpoint_url = amazon_bedrock_endpoint_url)

''' 
import json

def format_text_claude(text):
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

	if type == 'titan':
		print("**THE LLM TYPE IS -->" + type)
		#Test for invoke model begins
		parameters = {
			"maxTokenCount":512,
			"stopSequences":[],
			"temperature":0,
			"topP":0.9
		}
		body = json.dumps({"inputText": prompt, "textGenerationConfig": parameters})
		modelId = "amazon.titan-tg1-large" #"amazon.titan-tg1-large"
		accept = "application/json"
		contentType = "application/json"
		print("prompt---->" + prompt)

		response = bedrock_client.invoke_model(
			body=body, modelId=modelId, accept=accept, contentType=contentType
		)

		response_body = json.loads(response.get("body").read())

		response_text_titan = response_body.get("results")[0].get("outputText")

		return response_text_titan
	
	elif type == 'claude':
            print("**THE LLM TYPE IS -->" + type)
            formatted_prompt_claude = format_text_claude(prompt)
            print("*** Formatted text for claude ***")
            print("\n")
            print(formatted_prompt_claude)
            print("\n")
            prompt = formatted_prompt_claude
            body = json.dumps({"prompt": prompt,
                     "max_tokens_to_sample":300,
                     "temperature":1,
                     "top_k":250,
                     "top_p":0.999,
                     "stop_sequences":[]
                      }) 
            modelId = 'anthropic.claude-v2' # change this to use a different version from the model provider
            accept = 'application/json'
            contentType = 'application/json'
            print("prompt---->" + prompt)
            response = bedrock_client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
            response_body = json.loads(response.get('body').read())

            response_text_claude = response_body.get('completion')

            return response_text_claude
	
	elif type == 'jurassic':
		print("**THE LLM TYPE IS -->" + type)
		body = json.dumps({"prompt":prompt,"maxTokens":200,"temperature":0,"topP":1,"stopSequences":[],"countPenalty":{"scale":0},"presencePenalty":{"scale":0},"frequencyPenalty":{"scale":0}}) 
		modelId = 'ai21.j2-ultra' # change this to use a different version from the model provider
		accept = 'application/json'
		contentType = 'application/json'
		print("prompt---->" + prompt)
		response = bedrock_client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
		response_body = json.loads(response.get('body').read())


		response_text_jurassic = response_body.get('completions')[0].get("data").get("text")

		return response_text_jurassic

	elif type == 'llama':
            print("**THE LLM TYPE IS -->" + type)
            formatted_text_llama = format_text_llama(prompt)
            print("*** Formatted text for llama ***")
            print("\n")
            print(formatted_text_llama)
            print("\n")
            prompt = formatted_text_llama
            body = json.dumps({"prompt": prompt,"max_gen_len": 512,"temperature": 0.2,"top_p": 0.9}) 
            modelId = 'meta.llama2-13b-chat-v1' # change this to use a different version from the model provider
            accept = 'application/json'
            contentType = 'application/json'
            print("prompt---->" + prompt)
            response = bedrock_client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
            response_body = json.loads(response.get('body').read())

            response_text_llama = response_body.get('generation')

            return response_text_llama

	elif type == 'cohere':
		print("**THE LLM TYPE IS -->" + type)
		body = json.dumps({"prompt": prompt,"max_tokens": 100,"temperature": 0.8} ) 
		modelId = 'cohere.command-text-v14' # change this to use a different version from the model provider
		accept = 'application/json'
		contentType = 'application/json'
		print("prompt---->" + prompt)
		response = bedrock_client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
		response_body = json.loads(response.get('body').read())

		response_text_cohere = response_body.get('generations')[0].get("text")

		return response_text_cohere