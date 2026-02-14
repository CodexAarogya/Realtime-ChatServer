import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message = message + "   -- reply from server" # modify the message to indicate it's from the server
        self.send(text_data=json.dumps({        # for now,  echo the message back to the client
            'message': message
        }))

