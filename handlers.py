import yaml
import re
import requests
import time

from structures import Message

with open('config/config.yml', 'r') as configfile:
    config = yaml.safe_load(configfile)

with open(config['github_token'], 'r') as tokenfile:
    token = tokenfile.read().strip()


AUTH_HEADER = {'Authorization': f'token {token}'}
GH_ENDPOINT = 'https://api.github.com/'
RATELIMIT = 60*60*24 # 24 hours
ratelimits = {}

def on_message(client, message: Message):
    if f'<@{client.client_id}>' not in message.text: return
    content = message.text.strip()
    match = re.match(
        f"<@{client.client_id}> add ([^\s]+) to(?: the)? github.*",
        content
    )

    if match:
        if message.user in ratelimits and \
            ratelimits[message.user] + RATELIMIT > time.time():
            client.api_call(
                'chat.postMessage',
                channel=message.channel,
                text="To prevent abuse, you may not run this command frequently."
            )

        account = match.group(1)
        response = requests.put(
            GH_ENDPOINT + f'orgs/UofT-group-sideprojects/memberships/{account}',
            headers=AUTH_HEADER
        )
        payload = response.json()
        if response.status_code != 200:
            print(payload)
            answer = "Sorry, I can't do that D:"
        elif payload['state'] == 'pending':
            answer = f"An invite has been sent to {account} Check your email :)"
            ratelimits[message.user] = time.time()
        else:
            answer = f"{account} has already been invited"


        client.api_call(
            'chat.postMessage',
            channel=message.channel,
            text=answer
        )