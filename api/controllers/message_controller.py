from ..models.message_model import Message
from flask import request, session

class MessageController:
    """Clase de controlador de mensajes."""

    @classmethod
    def get_message(self, message_id):
        return Message.get_message(Message(
            message_id = message_id
        )).serialize(), 200
    
    @classmethod
    def get_messages(cls):
        messages = []
        if request.args.get('channel_id'):
            message_obj = Message(channel_id=request.args.get('channel_id'))
            print("MESSAGE OBJ:", message_obj.channel_id, message_obj.message, message_obj.channel_id)
            messages = Message.get_messages(message_obj)
        else:
            print("SEGUNDO GET")
            messages = Message.get_messages()
        return [message.serialize2() for message in messages], 200

    # @classmethod
    # def get_messages(self):
    #     print("LLEGO A GET_MESSAGES")
    #     message_objects = Message.get_messages()
    #     print("DESPUES DE GET_MESSAGES")
    #     messages = []
    #     for message in message_objects:
    #         messages.append(message.serialize())
    #     return messages, 200

    @classmethod
    def create_message(self):
        print("CREATE MESSAGE - CONTROLLER")
        data = request.json
        message = Message(
            message = data.get('message'),
            user_id = session.get('user_id'),
            channel_id = data.get('channel_id')
        )
        Message.create_message(message)

        return {}, 201
    
    @classmethod
    def update_message(self, message_id,message):
        userConectado=session.get('username')#usuario logeado
        userMensaje=Message.getUserBy_id(message_id)#usuario del mensaje
        print("Hola, este es el usuario que creo el mensaje -->",userMensaje.username)
        if userConectado==userMensaje.username:
            m=Message(message_id=message_id,message=message)
            if m.message!=None:
                Message.update_message(m)
                return {"message":"Mensaje editado."},200
        else:
            return {"message":"Usted no puede EDITAR este mensaje"},403
    
    @classmethod
    def delete_message(self, message_id):
        message = Message(message_id=message_id)
        Message.delete_message(message)

        return {}, 200
    
    @classmethod
    def eliminarMensaje(self,idMensaje):
        userConectado=session.get('username')#usuario logeado
        userMensaje=Message.getUserBy_id(idMensaje)#usuario del mensaje
        print("Hola, este es el usuario que creo el mensaje -->",userMensaje.username)
        if userConectado==userMensaje.username:
            message = Message(message_id=idMensaje)
            Message.delete_message(message)
            return {"message":"Mensaje Eliminado"},200
        else:
            return {"message":"Usted no puede ELIMINAR este mensaje"},403