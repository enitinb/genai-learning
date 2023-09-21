# LLM Type selection in code

Amazon Bedrock is a fully managed service that makes foundation models (FMs) from Amazon and leading AI startups available through an API, so you can choose from various FMs to find the model that's best suited for your use case. With the Amazon Bedrock serverless experience, you can quickly get started, easily experiment with FMs, privately customize FMs with your own data, and seamlessly integrate and deploy them into your applications using AWS tools and capabilities. 
 
Different type of foundation models have different parameters and also response structure with which you can interact. In this we will look into Amazon Titan, Claude and Jurrasic as an example from a python code perspective. 

Below are examples of API requests. Please note "body" and how the request structure can differ.

Titan 

```
{
  "modelId": "amazon.titan-tg1-large",
  "contentType": "application/json",
  "accept": "*/*",
  "body": {
   "inputText": "this is where you place your input text",
   "textGenerationConfig": {
      "maxTokenCount": 8192,
      "stopSequences": [],
      "temperature":0,
      "topP":1
     }
   } 
}
```

Claude
```
{
  "modelId": "anthropic.claude-v2",
  "contentType": "application/json",
  "accept": "*/*",
  "body": "{"prompt":"this is where you place your input text","max_tokens_to_sample":1,"temperature":0.5,"top_k":250,"top_p":0.5,"stop_sequences":[]}"  
}
```

Jurrasic
```
{
  "modelId": "ai21.j2-ultra",
  "contentType": "application/json",
  "accept": "*/*",
  "body": "{"prompt":"this is where you place your input text","maxTokens":200,"temperature":0,"topP":1,"stopSequences":[],"countPenalty":{"scale":0},"presencePenalty":{"scale":0},"frequencyPenalty":{"scale":0}}"  
}
```

In this util I have written two versions to handle this. First version using python's [ConfigParser](https://docs.python.org/3/library/configparser.html) module and other is a standalone function with conditional statements. 

There are two modules you can import. As of now you can have the module file in the same location as your client or you can enhance it to be kept into your own module folders. 

```
import amz_brck_llm_cfg
amz_brck_llm_cfg.interactWithLLM(prompt,llm_type,bedrock_client)
```
or 
```
import amz_brck_llm
amz_brck_llm.interactWithLLM(prompt,llm_type,bedrock_client)

```

Note :     
- prompt : Prompt to pass 
- llm_type : LLM type value to use, currently supports titan, claude and jurrasic
- bedrock_client : boto3 client, example : boto3.client('bedrock' , region, endpoint_url = amazon_bedrock_endpoint_url)

Below are the details of both modules **amz_brck_llm_cfg**  and **amz_brck_llm** 

1. **amz_brck_llm_cfg** :  Python [ConfigParser](https://docs.python.org/3/library/configparser.html) module - This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily. [amz_brck_llm_cfg](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llmTypeSelect_Configparser.py) is the module file which refers to the configuration file [llm_config.ini](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llm_config.ini). This reduces a lot of conditional coding for you. You can a test client file [testClient_amz_brck_llm_cfg.py](testClient_amz_brck_llm_cfg) to test the module
2. **amz_brck_llm** :  Regular python code to manage the selection. [llmTypeSelect.py](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llmTypeSelect.py)

**Note** : Added for Titan, Claude and Jurrassic as of now. You can easily add support for other LLM from Amazon Bedrock

You may still have to do some conditional coding based on the response is provided by the iteration over objects. Below is an example from the helper code which uses ConfigParser

```
    if type == 'titan':
        response_text_titan = response_body.get("results")[0].get("outputText")
        return response_text_titan
    elif type == 'claude':
        response_text_claude = response_body.get('completion')
        return response_text_claude
    elif type == 'jurrasic':
        response_text_jurrasic = response_body.get('completions')[0].get("data").get("text")
        return response_text_jurrasic
```
