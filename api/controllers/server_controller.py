from ..models.server_model import Server
from flask import request

class ServerController:
    """Clase de controlador de servidores"""

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