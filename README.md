# SNS Notification API (AWS Lambda + SNS)

This project is a serverless notification service that sends real-time messages (email/SMS) via AWS SNS when triggered through an API Gateway.

## Tech Stack

- AWS Lambda
- Amazon SNS
- API Gateway
- AWS SAM (Serverless Framework)
- Python (boto3)

## Features

- Sends notification to a predefined SNS topic.
- API Gateway triggers Lambda.
- Environment variable driven.

##  API Endpoint

*POST* /notify

*Body:*
```json
{
  "message": "Hello from SNS!",
  "subject": "Test Notification"
}
