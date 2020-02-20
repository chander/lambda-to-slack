"""Environment configuration values used by lambda functions."""

import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
SLACK_URL = os.getenv('SLACK_URL')
SLACK_URL1 = os.getenv('SLACK_URL1')
SLACK_URL2 = os.getenv('SLACK_URL2')
CONTAINS_STRING1 = os.getenv('CONTAINS_STRING1')
CONTAINS_STRING2 = os.getenv('CONTAINS_STRING2')
