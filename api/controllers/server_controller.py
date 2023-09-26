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
        username = session.get('username')
        user_obj = User.get(User(username=username))
        admin_user = user_obj.user_id
        data = request.json
        server_obj = Server(name=data.get('name'), description=data.get('description'), admin_user=admin_user)
        Server.create_server(server_obj)

        Server.create_us(admin_user)

        return {}, 201
    
    @classmethod
    def get_servers_user(cls):
        #print("Estoy en get_servers_user")
        username = session.get('username')
        user_obj = User.get(User(username=username))
        #print("OBJETO USER: ", user_obj.serialize())
        server_obj = Server.get_server_user(user_obj)
        
        servers = []
        if servers is not None:
            for server in server_obj:
                servers.append(server.serialize())
            return servers, 200
        else:
            return {'msg':'Únete a un servidor'}, 404