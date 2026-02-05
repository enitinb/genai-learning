# This document provides background context to guide how work is done during the construction phase.

## Python Code Standards (Simple)

- Keep code easy to read and easy to understand
- Use clear, descriptive names
- Keep functions small and focused
- Prefer straightforward logic over abstractions
- Separate core logic from API or framework code
- Handle invalid input clearly and predictably

## AWS Deployment Defaults (Simple, Serverless)

- Use a serverless approach for simplicity
- Prefer AWS SAM templates for infrastructure definition
- Use Amazon API Gateway for REST APIs
- Use AWS Lambda for backend compute
- Use Amazon S3 for static website hosting
- Use CloudWatch Logs for basic logging
- Apply least-privilege IAM roles
- Keep infrastructure minimal and workshop-friendly
