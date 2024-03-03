# Generating Image Descriptions using Amazon Rekognition and Amazon Bedrock

This sample uses Amazon Rekognition and Amazon Bedrock to automatically generate text descriptions for images. 

It follows a two-step process:

1. **Image Label extraction**: Amazon Rekognition is used to detect labels present in an input image. These labels with high confidence scores are extracted.

2. **Text Generation**: The extracted labels are then formatted into a prompt which is passed to a large language model (LLM) from Amazon Bedrock. The LLM generates a paragraph summarizing the image content.

By combining computer vision and natural language processing, this can produce human readable descriptions explaining the key elements within an image. It has applications for auto-alt text, assisting visually impaired users, and more.

The code handles passing images to Amazon Rekognition, parsing the response, selecting relevant labels, constructing prompts, interacting with the Bedrock LLM APIs, and outputting the generated text descriptions. It also converts the final output to an audio file. 
