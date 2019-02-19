from structures import Message

def on_message(client, message: Message):
    if f'<@{client.client_id}>' in message.text:
        client.api_call(
            'chat.postMessage',
            channel=message.channel,
            text='Hello!'
        )