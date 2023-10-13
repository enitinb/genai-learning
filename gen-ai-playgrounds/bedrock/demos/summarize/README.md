# 📣 AWS Announcements Assistant 🤖

Evaluate 🔎 AWS Announcements and auto-generate a presentation. This system will fetch 🎣 latest AWS annoucements, using LLM will summarize the details and extract technology names from the details and auto-generate a presentation for you.


1.	The process starts by downloading the latest AWS announcement from the public URLs.
2.	The user selects the date for which announcements need to be pulled.
3.	The process reads the announcements one by one for that date and prepares them to be passed to Amazon Bedrock.
4.	For each announcement, the parsed HTML text of the announcement details is passed in the prompt to Amazon Bedrock.
5.	Based on the selected large language model (Amazon Titan or Claude), 2 key takeaways and entity (technology name) extraction are done by the model to be included in the PPT. 
6.	The response from the LLM is returned to the process which then orchestrates the responses further
7.	The prompt and the response from the LLM are saved to a DynamoDB for analysis and future caching purposes.
9.	The key takeaways and extracted technology names are converted to a PowerPoint presentation and saved.

![Alt text](announcement_assist_arch.png)


# Pre-requisite 

```
!pip install bs4
!pip install requests 
!pip install langchain
!pip install python-pptx
```

**Note** : The notebook currently access the following services, ensure you have required IAM permissions to run the following

1. Amazon Bedrock - This is used to interact with the foundation models 
2. Amazon DynamoDB - This is used to save the prompt and its response 




