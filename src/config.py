"""Environment configuration values used by lambda functions."""

import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
SLACK_URL = os.getenv('SLACK_URL')
MESSAGE_CONFIGS = []
for I in range(1, 21):
    slack_url = os.getenv(f'SLACK_URL{str(I).zfill(2)}', None)
    contains_string = os.getenv(f'CONTAINS_STRING{str(I).zfill(2)}', None)
    if slack_url and contains_string:
        MESSAGE_CONFIGS.append((slack_url, contains_string))
    else:
        break
