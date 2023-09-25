from ..database import DatabaseConnection

class Server:
    """Clase que representa un servidor."""

    def __init__(self, **kwargs):
        self.server_id = kwargs.get('server_id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.admin_user = kwargs.get('admin_user')

    def __str__(self):
        return f"Server: {self.name}"
    
    def serialize(self):
        return {
            "server_id": self.server_id,
            "name": self.name,
            "description": self.description, 
            "admin_user": self.admin_user,
        }

    @classmethod
    def create_server(cls, server):
        """Crea un servidor."""
        sql = """INSERT INTO discord.servers (name, description, admin_user) VALUES (%(name)s, %(description)s, %(admin_user)s);"""
        params = server.__dict__
        DatabaseConnection.execute_query(sql, params=params)

        return {"message": "Servidor Registrado con exito!"}, 201
    
    @classmethod
    def create_us(cls, user_admin):
        """Crea registro que relaciona un servidor con un usuario."""
        sql = """INSERT INTO discord.server_user (server_id, user_id) SELECT MAX(servers.server_id), %s FROM discord.servers;"""
        params = user_admin,
        DatabaseConnection.execute_query(sql, params=params)  

    @classmethod
    def delete_server(cls, server):
        query = "DELETE FROM discord.servers WHERE server_id = %s"
        params = (server.server_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_servers(self, server=None):
        """Funcion que retorna todos los servidores de la base de datos en formato JSON"""
        if server and server.server_id:
            query = "SELECT server_id, name, description, admin_user FROM discord.servers WHERE server_id = %s"
            params = (server.server_id,)
            result = DatabaseConnection.fetch_one(query, params)
            if result:
                return Server(
                    server_id = result[0],
                    name = result[1],
                    description = result[2],
                    admin_user = result[3]
                )
            else:
                return None
        else:
            query = "SELECT server_id, name, description, admin_user FROM discord.servers"
            results = DatabaseConnection.fetch_all(query)
            
            servers = []
            if results is not None:
                for result in results:
                    servers.append(Server(
                        server_id=result[0],
                        name=result[1],
                        description=result[2],
                        admin_user=result[3]
                    ))
            return servers
    
    @classmethod
    def get_server_user(cls, user = None):
        """Funcion que retorna los servidores de un usuario de la base de datos."""
        print("llego al model")
        print("USER Y USER_USER_ID", user, user.user_id)
        if user and user.user_id:
            print("ENTRO AL IF")      
            query="""
            SELECT
                servers.server_id, servers.name, servers.description, servers.admin_user
            FROM
                discord.servers
            JOIN
                discord.server_user
            ON
                server_user.server_id = servers.server_id 
            JOIN
                discord.users
            ON
                users.user_id = server_user.user_id
            WHERE
                users.username = %(username)s;
            """
            print("USUARIOOO", user.username)
            params = user.__dict__
            results = DatabaseConnection.fetch_all(query, params=params)
            print("RESULTADOSSS", results)
            servers = []
            if results is not None:
                for result in results:
                    servers.append(Server(
                        server_id=result[0],
                        name=result[1],
                        description=result[2],
                        admin_user=result[3]
                    ))
            print("SERVERSSS:", servers[0].name)
            return servers