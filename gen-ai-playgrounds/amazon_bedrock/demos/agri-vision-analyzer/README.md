# AgriVision Analyzer

> **Important Note**: This project demonstrates how to integrate Amazon Bedrock's Nova video understanding capabilities into a real-world application. While fully functional, this deployment guide is intended for getting started and proof-of-concept purposes. For production deployments, additional considerations such as enhanced security controls, CI/CD pipelines, monitoring, high availability, and other enterprise requirements should be implemented based on your specific needs.

AgriVision Analyzer is a serverless web application that leverages  Amazon Bedrock's Nova-Lite to analyze agricultural videos. The application provides an intuitive interface for uploading videos, customizing analysis prompts, and maintaining a history of all analyses performed.

Amazon Nova Understanding Models are multimodal understanding models, that means they support multimodal inputs such as images, videos, and documents to infer and answer question based on the content provided. The Amazon Nova model family is equipped with novel vision capabilities that enable the model to comprehend and analyze images, documents, and videos thereby realizing multimodal understanding use cases. The Amazon Nova models allow you to include a single video in the payload, which can be provided either in base64 format or through an Amazon S3 URI. When using the base64 method, the overall payload size must remain within 25MB. However, you can specify an Amazon S3 URI for video understanding. This approach enables you to leverage the model for longer videos (up to 1GB in size) without being constrained by the overall payload size limitation. Amazon Nova models can analyze the passed video and answer questions, classify a video, and summarize information in the video based on provided instructions.

Reference : https://docs.aws.amazon.com/nova/latest/userguide/modalities.html 

## Features

- 🎥 Drag-and-drop video upload interface
- 🤖 AI-powered video analysis using Amazon Bedrock's Nova-Lite model
- ✨ Custom prompt support for specialized analysis needs
- 📊 Comprehensive analysis history tracking
- 🔐 Secure file handling with pre-signed URLs
- 🎯 Real-time analysis status updates
- 📱 Responsive design for all devices

## Architecture

The application is built using the following AWS services:

- **Amazon S3**: Stores uploaded videos with lifecycle management
- **Amazon DynamoDB**: Stores analysis results and metadata
- **AWS Lambda**: Handles video analysis, history and generates pre-signed URLs
- **Amazon API Gateway**: Provides RESTful API endpoints
- **Amazon Bedrock**: Performs video analysis using the Nova-Lite model
- **AWS SAM**: Infrastructure as Code for deployment

## Prerequisites

- AWS Account with appropriate permissions
- AWS SAM CLI installed
- Python 3.12 or later
- Node.js and npm (for frontend development)
- AWS CLI configured with your credentials

## Deployment Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/enitinb/genai-learning.git
   cd /genai-learning/gen-ai-playgrounds/amazon_bedrock/demos/agri-vision-analyzer
   ```

2. **Install Dependencies**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Configure AWS SAM**
   ```bash
   # Build the SAM application
   sam build

   # Deploy the application
   sam deploy --guided
   ```

   Follow the prompts and provide the following information:
   - Stack Name (e.g., agrivision-analyzer)
   - AWS Region
   - Confirm changes before deployment
   - Allow SAM CLI to create IAM roles

4. **Configure Frontend**
   - Update the API endpoint URL in `index.html` and `history.html` with the deployed API Gateway URL
   - Upload the frontend files to your preferred hosting service (e.g., S3 static website hosting)

## Environment Variables

The following environment variables are required for lambda functions:

- `REGION`: AWS region (default: us-east-1)
- `UPLOAD_BUCKET`: S3 bucket name for video uploads
- `DYNAMODB_TABLE`: DynamoDB table name for storing analysis results

## API Endpoints

- `POST /get-presigned-url`: Generates pre-signed URLs for video uploads
- `POST /analyze`: Triggers video analysis using Bedrock
- `GET /history`: Retrieves analysis history

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Acknowledgments

- Amazon Bedrock team for providing the Nova-Lite model
- AWS SAM team for the serverless application framework

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
