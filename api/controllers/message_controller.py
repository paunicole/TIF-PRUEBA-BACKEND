from ..models.message_model import Message
from flask import request

class MessageController:
    """Clase de controlador de mensajes."""

    @classmethod
    def get_message(self, message_id):
        return Message.get_message(Message(
            message_id = message_id
        )).serialize(), 200
    
    @classmethod
    def get_messages(self):
        print("LLEGO A GET_MESSAGES")
        message_objects = Message.get_messages()
        messages = []
        for message in message_objects:
            messages.append(message.serialize())
        return messages, 200

    @classmethod
    def create_message(self):
        data = request.json
        message = Message(
            message = data.get('message')
        )
        Message.create_message(message)

        return {}, 201
    
    @classmethod
    def update_message(self, message_id):
        pass
    
    @classmethod
    def delete_message(self, message_id):
        message = Message(message_id=message_id)
        Message.delete_message(message)

        return {}, 200