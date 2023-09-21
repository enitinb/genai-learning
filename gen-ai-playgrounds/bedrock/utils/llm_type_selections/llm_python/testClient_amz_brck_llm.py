import amz_brck_llm

import time
import boto3

bedrock_client = boto3.client('bedrock' , 'us-west-2', endpoint_url = 'https://bedrock.us-west-2.amazonaws.com')

prompt  = """Amazon QuickSight introduces a range of exciting enhancements to KPI visual, including templated KPI layouts, support for sparklines, improvements in conditional formatting, and a revamped format pane. The KPI visual now offers a user-friendly onboarding experience, allowing authors to select from pre-designed KPI layouts tailored to various use cases and configurations. This empowers authors to effortlessly craft visually appealing KPIs with just a few clicks.Users can also gain insights into the trend of their KPIs over time by incorporating sparklines, which include line and area charts, in addition to progress bars. Furthermore, conditional formatting rules are now associated with specific fields, extending the capability to apply formatting rules independently to both the actual and comparison values, irrespective of which one is designated as the primary value. To accommodate these new additions seamlessly, the format pane has been redesigned, enhancing navigation and simplifying the process of setting font colors for metrics directly from the format pane, eliminating the necessity for conditional formatting. More details can be found here.The new KPI enhancements is now available in all supported Amazon QuickSight regions - US East (Ohio and N. Virginia), US West (Oregon), Asia Pacific (Mumbai, Seoul, Singapore, Sydney and Tokyo), Canada (Central), Europe (Frankfurt, Ireland and London), South America (São Paulo) and AWS GovCloud (US-West). See here for QuickSight regional endpoints.
Summarize the above in one sentence
	"""  

# Test code
response = amz_brck_llm.interactWithLLM(prompt,'claude',bedrock_client)

print("RESPONSE from : claude " + response)

time.sleep(2)

print("*******************")

response = amz_brck_llm.interactWithLLM(prompt,'titan',bedrock_client)

print("RESPONSE from : titan " + response)


print("*******************")

response = amz_brck_llm.interactWithLLM(prompt,'jurassic',bedrock_client)

print("RESPONSE from : jurassic " + response)