import time
import yaml

from slackclient import SlackClient

with open('config/config.yml', 'r') as configfile:
    config = yaml.safe_load(configfile)

with open(config['token'], 'r') as tokenfile:
    token = tokenfile.read()

client = SlackClient(token)
poll_rate = config['polling_frequency']

if client.rtm_connect(with_team_state=False):
    while client.server.connected:
        for event in client.rtm_read():
            print(event)

        time.sleep(poll_rate)
else:
    print('Connection Failed')