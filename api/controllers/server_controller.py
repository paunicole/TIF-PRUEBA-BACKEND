from ..models.server_model import Server
from ..models.users_model import User
from flask import request, session

class ServerController:
    """Clase de controlador de servidores."""

    @classmethod
    def get_servers(self):
        server_obj = Server.get_servers()
        servers = []
        for server in server_obj:
            servers.append(server.serialize())
        return servers, 200

    @classmethod
    def create_server(self):
        data = request.json
        print("NOMBREEEE", data.get('name'), data.get('description'))
        server_obj = Server(name=data.get('name'), description=data.get('description'))
        Server.create_server(server_obj)

        return {}, 201
    
    @classmethod 
    def get_servers_user(cls, username):
        servers = Server.get_server_user(User(username = username))
        
        if servers is not None:
            return servers.serialize(), 200
        else:
            return {'msg':'Únete a un servidor'}, 404