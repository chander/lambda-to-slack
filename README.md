[![](https://img.shields.io/badge/Available-serverless%20app%20repository-blue.svg)](https://serverlessrepo.aws.amazon.com/#/applications/arn:aws:serverlessrepo:us-east-1:289559741701:applications~lambda-to-slack)

# macnoms-lambda-to-slack

This serverless app posts messages to Slack.  It uses a set of contains strings to determine which slack channel/webhook 
should be used for the messages.  This is important because only a single subscriber is allowed for each cloudwatch
log; so logging to more than a single slack channel with a single lambda-to-slack (traditional) lambda was not possible.

## App Architecture

![App Architecture](https://github.com/keetonian/lambda-to-slack/raw/master/images/lambda-to-slack.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:289559741701:applications~lambda-to-slack) and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

## Using this Application

This lambda function expects to be called with a JSON array of strings, and will post each string to a Slack channel via a webhook.

### Slack Url
To get a webhook URL for this application:
* Navigate to https://api.slack.com
* Click on the "Start Building" button
* Give your app a name and select a workspace
* Under "Add features and functionality" select "Incoming Webhooks"
* Turn on "Incoming Webhooks" and click "Add New Webhook to Workspace"
* Select the desired channel and click "Authorize"
* Copy the generated Webhook URL

## App Parameters

1. `SlackUrl` (required) - Webhook URL for integration with Slack
1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO
1. `SlackUrl1` (required) - Webhook URL for integration with Slack (if messages match ContainsString1)
1. `ContainsString1` (required) - A string that, if present in the message, dictates that the message should be logged to SlackUrl2
1. `SlackUrl2` (required) - Webhook URL for integration with Slack (if messages match ContainsString1)
1. `ContainsString2` (required) - A string that, if present in the message, dictates that the message should be logged to SlackUrl2

## App Outputs

1. `LambdaToSlackName` - Lambda function name.
1. `LambdaToSlackArn` - Lambda function ARN.

## License Summary

This code is made available under the MIT license. See the LICENSE file.
