## AWS Serverless Sns Forwarder

This is a serverless app that receives a JSON array of strings and forwards them to an SNS topic.

## App Architecture

![App Architecture](https://github.com/awslabs/aws-serverless-sns-forwarder/raw/master/images/sns-forwarder.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~aws-serverless-sns-forwarder) and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

## App Parameters

1. `SnsTopicName` (required) - Name of SNS topic to publish messages to. This topic needs to be in the same account and same region as this application.
1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO

## App Outputs

1. `SnsForwarderFunctionName` - Name of the lambda function
1. `SnsForwarderFunctionArn` - Arn of the lambda function
1. `SnsForwarderFunctionDLQArn` - Arn of the lambda function's DLQ

## License Summary

This sample code is made available under the MIT license. 
