[![](https://img.shields.io/badge/Available-serverless%20app%20repository-blue.svg)](https://serverlessrepo.aws.amazon.com/#/applications/arn:aws:serverlessrepo:us-east-1:289559741701:applications~macnoms-lambda-to-slack)

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
1. `SlackUrl1` (optional) - Webhook URL for integration with Slack (if messages match ContainsString1)
1. `ContainsString1` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl1
1. `SlackUrl2` (optional) - Webhook URL for integration with Slack (if messages match ContainsString2)
1. `ContainsString2` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl2
1. `SlackUrl3` (optional) - Webhook URL for integration with Slack (if messages match ContainsString3)
1. `ContainsString3` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl3
1. `SlackUrl4` (optional) - Webhook URL for integration with Slack (if messages match ContainsString4)
1. `ContainsString4` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl4
1. `SlackUrl5` (optional) - Webhook URL for integration with Slack (if messages match ContainsString5)
1. `ContainsString5` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl5
1. `SlackUrl6` (optional) - Webhook URL for integration with Slack (if messages match ContainsString6)
1. `ContainsString6` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl6
1. `SlackUrl7` (optional) - Webhook URL for integration with Slack (if messages match ContainsString7)
1. `ContainsString7` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl7
1. `SlackUrl8` (optional) - Webhook URL for integration with Slack (if messages match ContainsString8)
1. `ContainsString8` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl8
1. `SlackUrl9` (optional) - Webhook URL for integration with Slack (if messages match ContainsString9)
1. `ContainsString9` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl9
1. `SlackUrl10` (optional) - Webhook URL for integration with Slack (if messages match ContainsString10)
1. `ContainsString10` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl10
1. `SlackUrl11` (optional) - Webhook URL for integration with Slack (if messages match ContainsString11)
1. `ContainsString11` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl11
1. `SlackUrl13` (optional) - Webhook URL for integration with Slack (if messages match ContainsString12)
1. `ContainsString12` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl12
1. `SlackUrl13` (optional) - Webhook URL for integration with Slack (if messages match ContainsString13)
1. `ContainsString13` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl13
1. `SlackUrl14` (optional) - Webhook URL for integration with Slack (if messages match ContainsString14)
1. `ContainsString14` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl14
1. `SlackUrl15` (optional) - Webhook URL for integration with Slack (if messages match ContainsString15)
1. `ContainsString15` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl15
1. `SlackUrl16` (optional) - Webhook URL for integration with Slack (if messages match ContainsString16)
1. `ContainsString16` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl216
1. `SlackUrl17` (optional) - Webhook URL for integration with Slack (if messages match ContainsString17)
1. `ContainsString17` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl17
1. `SlackUrl18` (optional) - Webhook URL for integration with Slack (if messages match ContainsString18)
1. `ContainsString18` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl18
1. `SlackUrl19` (optional) - Webhook URL for integration with Slack (if messages match ContainsString19)
1. `ContainsString19` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl19
1. `SlackUrl20` (optional) - Webhook URL for integration with Slack (if messages match ContainsString20)
1. `ContainsString20` (optional) - A string that, if present in the message, dictates that the message should be logged to SlackUrl20

## App Outputs

1. `LambdaToSlackName` - Lambda function name.
1. `LambdaToSlackArn` - Lambda function ARN.

## License Summary

This code is made available under the MIT license. See the LICENSE file.
