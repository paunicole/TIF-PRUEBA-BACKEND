from ..models.server_model import Server
from ..models.users_model import User
from flask import request, session

class ServerController:
    """Clase de controlador de servidores."""

    @classmethod
    def get_servers(cls):
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
    def create_server_explore(self):
        data = request.json
        Server.create_us_2(server_id=data.get('server_id'), user_id = session.get('user_id'))

        return {}, 201
    
    @classmethod
    def get_servers_user(cls):
        username = session.get('username')
        print("VINO POR GET_SERVERS_USER - SERVER CONTROLLER", username)
        user_obj = User.get(User(username=username))
        print("OBJETO USER: ", user_obj.serialize())
        server_obj = Server.get_servers(user_obj)
        
        servers = []
        if servers is not None:
            for server in server_obj:
                servers.append(server.serialize())
            return servers, 200
        else:
            return {'msg':'Únete a un servidor'}, 404
    
    @classmethod
    def get_count(cls, server_id):
        print("LLEGO A COUNT CONTROLADOR")
        count = Server.get_server_by_id(server_id)
        print("CONTADOR: ", count)
        return {"count": count}, 200