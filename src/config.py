"""Environment configuration values used by lambda functions."""

import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
SLACK_URL = os.getenv('SLACK_URL')
MESSAGE_CONFIGS=[]
for I in range(1, 21):
    slack_url=os.getenv(f'SLACK_URL{I}', None)
    contains_string = os.getenv(f'CONTAINS_STRING{I}', None)
    if slack_url and contains_string:
        MESSAGE_CONFIGS.append((contains_string, slack_url))
    else:
        break

