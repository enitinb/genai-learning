# RAG with Bedrock

This demo show cases RAG use case using Amazon Bedrock model Titan. The code uses Titan but it can be tailored to other models as as well. The code also uses Titan's embedding model to create embeddings and store a vector store FAISS. At a high level it does the following 

1. Parses pdf, creates embedding and stores to in-memory Vector Store FAISS. You can use any vector store of your choice. This is for demo 
2. Takes user prompts, searches the store, gets the result and pass to LLM for final output. 


# Prerequisites

* Please follow the set up instructions which can be referenced [Amazon Bedrock boto3 Setup](https://github.com/aws-samples/amazon-bedrock-workshop/blob/main/00_Intro/bedrock_boto3_setup.ipynb)
* The sample code here assumes that you have AWS credentials on your local machine or appropiate IAM roles set up with required access. 
* The code uses [gradio](https://www.gradio.app/) to create the front end for this. You can use any other front of your choice. 

# Installed versions

The demo code uses the following versions installed by ```pip install```

* langchain 0.0.256
* gradio    3.39.0


For below , these would be aligned with [Amazon Bedrock boto3 Setup](https://github.com/aws-samples/amazon-bedrock-workshop/blob/main/00_Intro/bedrock_boto3_setup.ipynb)

* boto3     1.28.21
* botocore  1.31.21
* awscli    1.29.21


