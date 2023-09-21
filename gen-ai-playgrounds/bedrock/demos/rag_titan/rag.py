import os
from langchain.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain.llms.bedrock import Bedrock

import random


import gradio as gr

llm_region_name = 'LLM_AWS_REGION' #Change per your settings
llm_endpoint_url = 'LLM_ENDPOINT_URL'#Change per your settings
llm_model_id = 'LLM_MODLE_ID'#Change per your settings

embedding_region_name = 'EMBEDDING_AWS_REGION'#Change per your settings
embedding_endpoint_url = 'EMBEDDING_ENDPOINT_URL'#Change per your settings
embedding_model_id = 'EMBEDDING_MODLE_ID'#Change per your settings



def get_llm():
    
    model_kwargs =  { 
        "maxTokenCount": 1024, 
        "stopSequences": [], 
        "temperature": 0, 
        "topP": 0.9 
    }

    llm = Bedrock( #create a Bedrock llm client
        region_name = llm_region_name, #sets the region name (if not the default)
        endpoint_url = llm_endpoint_url, #sets the endpoint URL (if necessary)
        model_id = llm_model_id, #use the Titan model
        model_kwargs=model_kwargs
        )
    
    return llm


def get_index(): #creates and returns an in-memory vector store to be used in the application
    

    embeddings = BedrockEmbeddings(
        region_name = embedding_region_name, #sets the region name (if not the default)
        endpoint_url = embedding_endpoint_url, #sets the endpoint URL (if necessary)
        model_id = embedding_model_id, #use the Titan model
    ) #create a Titan Embeddings client
    
    pdf_path = "TriNet_Microservices_POC_Design Patterns and_Options.pdf" #assumes local PDF file with this name

    #loader = PyPDFLoader(file_path=pdf_path) #load the pdf file
    loader = PyPDFDirectoryLoader("./data/")
    
    text_splitter = RecursiveCharacterTextSplitter( #create a text splitter
        separators=["\n\n", "\n", ".", " "], #split chunks at (1) paragraph, (2) line, (3) sentence, or (4) word, in that order
        #chunk_size=2000, #divide into 2000-character chunks using the separators above
        chunk_size=1024, #divide into 1024-character chunks using the separators above
        chunk_overlap=100 #number of characters that can overlap with previous chunk
    )
    
    index_creator = VectorstoreIndexCreator( #create a vector store factory
        vectorstore_cls=FAISS, #use an in-memory vector store for demo purposes
        embedding=embeddings, #use Titan embeddings
        text_splitter=text_splitter, #use the recursive text splitter
    )
    
    index_from_loader = index_creator.from_loaders([loader]) #create an vector store index from the loaded PDF
    
    return index_from_loader #return the index to be cached by the client app

index = get_index()
llm = get_llm()

def get_rag_response(question): #rag client function

    response_text = index.query(question=question, llm=llm) #search against the in-memory index, stuff results into a prompt and send to the llm
    
    return response_text

def random_response(message, history):
    print(message)
    return get_rag_response(message)

with gr.Blocks() as demo:

    gr.Markdown(
        """
        # Amazon Bedrock Demo 1
        **This is a demo of Amazon Bedrock using Titan Embedding and Titan LLM**.
        """)

    #gr.Interface(fn=get_rag_response, inputs="text", outputs="text")
    gr.ChatInterface(random_response)
        
demo.launch()  

