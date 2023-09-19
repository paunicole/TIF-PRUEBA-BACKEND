from ..models.channel_model import Channel
from flask import request

from ..models.exceptions import NotFound, BadRequest

class ChannelController:

    @classmethod
    def get(cls):
        channels = []
        if request.args.get('server_id'):
            channel_obj = Channel(server_id=request.args.get('server_id'))
            print("CHANNEL OBJ:", channel_obj.channel_id, channel_obj.name, channel_obj.server_id)
            channels = Channel.get(channel_obj)
        else:
            print("SEGUNDO GET")
            channels = Channel.get()
        return [channel.serialize() for channel in channels], 200

    @classmethod
    def get_by_id(cls, channel_id):
        if channel_id <= 0:
            raise BadRequest("El id de la tarea debe ser mayor a 0") 
        channel_obj = Channel(channel_id=channel_id)
        channel = Channel.get(channel_obj)
        if channel:
            return channel.serialize(), 200
        raise NotFound("Tarea no encontrada")

    @classmethod
    def create(cls):
        data = request.json
        channel_obj = Channel(
            name=data.get('name'),
            description=data.get('description'),
            server_id=data.get('server_id')
            )
        Channel.create(channel_obj)
        return {'message': 'Channel created successfully'}, 201

    @classmethod
    def delete(cls, channel_id):
        channel_obj = Channel(channel_id=channel_id)
        Channel.delete(channel_obj)
        return {'message': 'Channel deleted successfully'}, 200