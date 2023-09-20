import time
from langchain import PromptTemplate
import json
import boto3
import configparser

bedrock_client = boto3.client('bedrock' , 'us-west-2', endpoint_url = 'https://bedrock.us-west-2.amazonaws.com')


prompt  = """	
	Amazon QuickSight introduces a range of exciting enhancements to KPI visual, including templated KPI layouts, support for sparklines, improvements in conditional formatting, and a revamped format pane. The KPI visual now offers a user-friendly onboarding experience, allowing authors to select from pre-designed KPI layouts tailored to various use cases and configurations. This empowers authors to effortlessly craft visually appealing KPIs with just a few clicks.Users can also gain insights into the trend of their KPIs over time by incorporating sparklines, which include line and area charts, in addition to progress bars. Furthermore, conditional formatting rules are now associated with specific fields, extending the capability to apply formatting rules independently to both the actual and comparison values, irrespective of which one is designated as the primary value. To accommodate these new additions seamlessly, the format pane has been redesigned, enhancing navigation and simplifying the process of setting font colors for metrics directly from the format pane, eliminating the necessity for conditional formatting. More details can be found here.The new KPI enhancements is now available in all supported Amazon QuickSight regions - US East (Ohio and N. Virginia), US West (Oregon), Asia Pacific (Mumbai, Seoul, Singapore, Sydney and Tokyo), Canada (Central), Europe (Frankfurt, Ireland and London), South America (São Paulo) and AWS GovCloud (US-West). See here for QuickSight regional endpoints.
Summarize the above in one sentence
	"""  

config = configparser.ConfigParser()
config.read('llm_config.ini')

def interactWithLLM(prompt,type):

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
    response_body = json.loads(response.get("body").read())

    if type == 'titan':
        response_text_titan = response_body.get("results")[0].get("outputText")
        return response_text_titan
    elif type == 'claude':
        response_text_claude = response_body.get('completion')
        return response_text_claude
	


# Test code
response = interactWithLLM(prompt,'claude')

print("RESPONSE : " + response)

time.sleep(2)

print("*******************")

response = interactWithLLM(prompt,'titan')

print("RESPONSE : " + response)
