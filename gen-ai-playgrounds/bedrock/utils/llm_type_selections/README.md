# LLM Type selection in code

Amazon Bedrock is a fully managed service that makes foundation models (FMs) from Amazon and leading AI startups available through an API, so you can choose from various FMs to find the model that's best suited for your use case. With the Amazon Bedrock serverless experience, you can quickly get started, easily experiment with FMs, privately customize FMs with your own data, and seamlessly integrate and deploy them into your applications using AWS tools and capabilities. 
 
Different type of foundation models have different parameters and also response structure with which you can interact. In this we will look into Amazon Titan and Claude as an example from a python code perspective. 

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
Claud
```
{
  "modelId": "anthropic.claude-v2",
  "contentType": "application/json",
  "accept": "*/*",
  "body": "{"prompt":"this is where you place your input text","max_tokens_to_sample":1,"temperature":0.5,"top_k":250,"top_p":0.5,"stop_sequences":[]}"  
}
```

In this util I have written two versions to handle this. With this your calling code will only call the helper function **interactWithLLM(prompt,llm_type) --> lly_type value 'titan' or 'claud'**. example shown below

```
interactWithLLM(prompt,'claud')
interactWithLLM(prompt,'titan')
```

**Note** : Added for Titan and Claude as of now. You can easily add support for other LLM from Amazon Bedrock

1. Python [ConfigParser](https://docs.python.org/3/library/configparser.html) module - This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily. [llmTypeSelect_Configparser.py](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llmTypeSelect_Configparser.py) and configuration file [llm_config.ini](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llm_config.ini). This reduces a lot of conditional coding for you. 
2. Regular python code to manage the selection. [llmTypeSelect.py](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llmTypeSelect.py)

You may still have to do some conditional coding based on the response is provided by the iteration over objects. Below is an example from the helper code which uses ConfigParser

```
    if type == 'titan':
        response_text_titan = response_body.get("results")[0].get("outputText")
        return response_text_titan
    elif type == 'claud':
        response_text_claud = response_body.get('completion')
        return response_text_claud
```
