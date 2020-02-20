"""Lambda function handler."""

# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import config
import lambdalogging
import slack
from exceptions import InputError

LOG = lambdalogging.getLogger(__name__)


def post_to_slack(event, context):
    """Lambda function handler."""
    LOG.info('Received event: %s', event)

    if not isinstance(event, list):
        raise InputError(event, "Input needs to be a json array")

    for message in event:
        for slack_url, contains_string in config.MESSAGE_CONFIGS:
            if contains_string in message:
                slack.post_message(slack_url, message)
                break
    else:
        slack.post_message(config.SLACK_URL, message)
