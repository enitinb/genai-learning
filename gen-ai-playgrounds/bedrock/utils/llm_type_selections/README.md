# LLM Type selection in code

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon via a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. Using Amazon Bedrock, you can easily experiment with and evaluate top FMs for your use case, privately customize them with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), and build agents that execute tasks using your enterprise systems and data sources. Since Amazon Bedrock is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy generative AI capabilities into your applications using the AWS services you are already familiar with.
 
Different type of foundation models have different request parameters and also response structure with which you can interact. In this we will look into some of text models currently offered by Amazon Bedrock which includes below and see how we can use a re-usable python module to manage the input and output parameters. 
- [Amazon Titan](https://aws.amazon.com/bedrock/titan/)
- [Anthropic Claude](https://aws.amazon.com/bedrock/claude/)
- [AI21labs Jurrasic-2](https://aws.amazon.com/bedrock/jurassic/)
- [Llama 2](https://aws.amazon.com/bedrock/llama-2/)
- [Cohere](https://aws.amazon.com/bedrock/cohere-command/) 

Below are examples of API requests. Please note "body" and how the request structure can differ.

Amazon Titan 

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

Anthropic Claude
```
{
  "modelId": "anthropic.claude-v2",
  "contentType": "application/json",
  "accept": "*/*",
  "body": "{"prompt":"this is where you place your input text","max_tokens_to_sample":1,"temperature":0.5,"top_k":250,"top_p":0.5,"stop_sequences":[]}"  
}
```

AI21labs Jurassic-2
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

1. **amz_brck_llm_cfg** :  Python [ConfigParser](https://docs.python.org/3/library/configparser.html) module - This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in .INI files. You can use this to write Python programs which can be customized by end users easily. [amz_brck_llm_cfg](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llm_configparser/amz_brck_llm_cfg.py) is the module file which refers to the configuration file [llm_config.ini](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llm_configparser/llm_config.ini). This reduces a lot of conditional coding for you. You can a test notebook file [testClient_amz_brck_llm_cfg.ipynb](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llm_configparser/testClient_amz_brck_llm_cfg.ipynb) to test the module
2. **amz_brck_llm** : [amz_brck_llm](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llm_python/amz_brck_llm.py) is the module file which uses mostly conditional statements. You can a test client file [testClient_amz_brck_llm.py](https://github.com/bertieucbs/genai-learning/blob/main/gen-ai-playgrounds/bedrock/utils/llm_type_selections/llm_python/testClient_amz_brck_llm.py) to test the module

**Note** : Added for Titan, Claude, llama, cohere and Jurassic-2 as of now. You can easily add support for other LLM from Amazon Bedrock as it releases into the configuration files

You may still have to do some conditional coding based on the response is provided by the iteration over objects. Below is an example from the helper code which uses ConfigParser. Refer to the modules mentioned above. For now based on the available modules, I have added the support. 

```
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
```

Also some of the Models may require certain format of the prompt. Example Claude and Llama. The module has that support as an example 

```
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
```
