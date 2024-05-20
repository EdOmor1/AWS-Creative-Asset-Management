# Creative Asset Management

## Overview
This project builds a repository for storing and managing creative assets, automatically tagging and categorizing them using AWS services.

## Architecture
![Architecture Diagram](diagrams/architecture_diagram.png)

## AWS Services Used
- Amazon S3
- Amazon Rekognition
- AWS Lambda
- Amazon DynamoDB

## Features
- Automated tagging and categorization of creative assets.
- Scalable storage solution using Amazon S3.
- Integration with Amazon Rekognition for image analysis.

## Prerequisites
- AWS account

## Setup

### Step 1: Deploy Infrastructure
1. Deploy the CloudFormation stack using `infrastructure/cloudformation_template.yaml`.

### Step 2: Configure Lambda Functions
1. Update `src/asset_manager.py` with any necessary configurations.
2. Deploy the Lambda functions using the AWS Lambda console or AWS CLI.

## Usage
1. Upload creative assets to the designated S3 bucket.
2. The Lambda function `asset_manager.py` automatically tags and categorizes the assets.

## License
This project is licensed under the MIT License.
