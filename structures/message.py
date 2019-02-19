class Message:
    """
    Represents a slack message
    """
    def __init__(self, event):
        self.user = event.get('user', None)
        self.text = event.get('text', None)
        self.id = event.get('client_msg_id', None)
        self.team = event.get('team', None)
        self.channel = event.get('channel', None)
        self.timestamp = event.get('ts', event.get('event_ts', None))

    def to_dict(self):
        return {
            'user': self.user,
            'text': self.text,
            'client_msg_id': self.id,
            'team': self.team,
            'channel': self.channel,
            'event_ts': self.timestamp,
            'ts': self.timestamp
        }

    def __str__(self):
        return f'<Message user={self.user} ' \
               f'text={repr(self.text)} ' \
               f'channel={self.channel}>'

    def __repr__(self):
        return self.__str__()