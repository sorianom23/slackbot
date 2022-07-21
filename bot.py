import slack
import os
from dotenv import load_dotenv
from pathlib import Path


import ssl
import certifi
import urllib
from slack import WebClient
#from slack_sdk.errors import SlackApiError

ssl_context = ssl.create_default_context(cafile=certifi.where())

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'], ssl=ssl_context)

client.chat_postMessage(channel='#general', text='Hey!')
