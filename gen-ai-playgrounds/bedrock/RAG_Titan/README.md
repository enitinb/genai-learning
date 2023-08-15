# RAG with Bedrock

This demo show cases RAG use case using Amazon Bedrock model Titan. The code uses Titan but it can be tailored to other models as as well. The code also uses Titan's embedding model to create embeddings and store a vector store FAISS. 


# Prerequisites

* Please follow the set up instructions which can be referenced [Amazon Bedrock boto3 Setup](https://github.com/aws-samples/amazon-bedrock-workshop/blob/main/00_Intro/bedrock_boto3_setup.ipynb)
* The sample code here assumes that you have AWS credentials on your local machine or appropiate IAM roles set up with required access. 
* The code uses [gradio](https://www.gradio.app/) to create the front end for this. You can use any other front of your choice. 

