import time
import yaml
import logging

from structures import Message
from slackclient import SlackClient
from handlers import on_message

with open('config/config.yml', 'r') as configfile:
    config = yaml.safe_load(configfile)

with open(config['slack_token'], 'r') as tokenfile:
    token = tokenfile.read().strip()

client = SlackClient(token)
client.client_id = config['client_id']
logging.basicConfig(
    level=logging.INFO,
    format='[%(name)s %(levelname)s] %(message)s'
)
logger = logging.getLogger('slackbot')
poll_rate = config['polling_frequency']

if client.rtm_connect():
    while client.server.connected:
        for event in client.rtm_read():
            if event['type'] == 'hello': logger.info("Logged in!")
            elif event['type'] == 'message':
                try:
                    on_message(client, Message(event))
                except Exception as e:
                    logging.exception(
                        "During the handling of a message, "
                        "the following exception occured"
                    )

        time.sleep(poll_rate)
else:
    print('Connection Failed')