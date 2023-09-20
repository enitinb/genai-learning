import time
from langchain import PromptTemplate
import json
import boto3


bedrock_client = boto3.client('bedrock' , 'us-west-2', endpoint_url = 'https://bedrock.us-west-2.amazonaws.com')


prompt  = """	
	Amazon QuickSight introduces a range of exciting enhancements to KPI visual, including templated KPI layouts, support for sparklines, improvements in conditional formatting, and a revamped format pane. The KPI visual now offers a user-friendly onboarding experience, allowing authors to select from pre-designed KPI layouts tailored to various use cases and configurations. This empowers authors to effortlessly craft visually appealing KPIs with just a few clicks.Users can also gain insights into the trend of their KPIs over time by incorporating sparklines, which include line and area charts, in addition to progress bars. Furthermore, conditional formatting rules are now associated with specific fields, extending the capability to apply formatting rules independently to both the actual and comparison values, irrespective of which one is designated as the primary value. To accommodate these new additions seamlessly, the format pane has been redesigned, enhancing navigation and simplifying the process of setting font colors for metrics directly from the format pane, eliminating the necessity for conditional formatting. More details can be found here.The new KPI enhancements is now available in all supported Amazon QuickSight regions - US East (Ohio and N. Virginia), US West (Oregon), Asia Pacific (Mumbai, Seoul, Singapore, Sydney and Tokyo), Canada (Central), Europe (Frankfurt, Ireland and London), South America (São Paulo) and AWS GovCloud (US-West). See here for QuickSight regional endpoints.
Summarize the above in one sentence
	"""  
    

def interactWithLLM(prompt,type):

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
	
	elif type == 'claud':
		print("**THE LLM TYPE IS -->" + type)
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

		response_text_claud = response_body.get('completion')

		return response_text_claud
	


response = interactWithLLM(prompt,'claud')

print("RESPONSE : " + response)

time.sleep(2)

print("*******************")

response = interactWithLLM(prompt,'titan')

print("RESPONSE : " + response)