from ..database import DatabaseConnection
from ..models.exceptions import UserNotFound

class User:
    def __init__(self):
        """esta vacio"""

    def __init__(self,**kwargs):
        self.user_id = kwargs.get('user_id')
        self.email = kwargs.get('email')
        self.username = kwargs.get('username')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.password = kwargs.get('password')
        self.birthdate = kwargs.get('birthdate')
        self.avatar=kwargs.get("avatar")

    # def __init__(self,user_id=None, email=None,username=None,firstname=None,last_name=None,password=None,date_of_birth=None,avatar=None):
    #     self.user_id =user_id
    #     self.email = email
    #     self.username = username
    #     self.first_name = firstname
    #     self.last_name = last_name
    #     self.password = password
    #     self.date_of_birth = date_of_birth
    #     self.avatar=avatar
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password
            ,"birthdate": self.birthdate
            # , "avatar":self.avatar
        }
    @classmethod
    def is_registered(cls, user):
        query = """SELECT user_id FROM discord.users 
        WHERE username = %(username)s and password = %(password)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls,user):  

        if user.exists(user.username):
            sql="""SELECT user_id,email,username,first_name,last_name, password, birthdate FROM discord.users
            WHERE users.username=%(username)s"""
            params = user.__dict__
            result = DatabaseConnection.fetch_one(sql, params=params)

            if result is not None:
                return cls(
                    user_id = result[0],
                    email= result[1],
                    username = result[2],  
                    first_name = result[3],
                    last_name=result[4],
                    password= result[5],
                    birthdate = result[6]
                    # , avatar= result[7]
                )
            return None

    
    def exists(self, username):
        sql="SELECT username FROM discord.users "
        results= DatabaseConnection.fetch_all(sql)

        # print(result) [('ivana',), ('nicole',), ('alberto',), ('pablo',), ('luffy',), ('Master',), ('luffy',)]s
        existe=False
        for n in results:
            for x in n:
                if x==username: 
                    existe=True  
        # print(existe)
        return existe

    @classmethod
    def createUser(cls,user):
        # cls.get(user)

        if user.exists(user.username):
            return None
        else: 
            params=None
            if user.birthdate=="":
                sql="""INSERT INTO discord.users(email,username,first_name,last_name,password) 
                VALUES(%(email)s,%(username)s,%(first_name)s,%(last_name)s,%(password)s)"""
                params= user.__dict__
            else:

                sql="""INSERT INTO discord.users(email,username,first_name,last_name,password,birthdate) 
                VALUES(%(email)s,%(username)s,%(first_name)s,%(last_name)s,%(password)s,%(birthdate)s)"""
                params= user.__dict__
            DatabaseConnection.execute_query(sql, params=params)
            return ""

    @classmethod
    def updateUser(cls, user):
        # print("desde el modelo ->", user.__dict__)
        query ="""
        UPDATE
            discord.users
        SET
            email = %(email)s,
            username = %(username)s,
            first_name = %(first_name)s,
            last_name = %(last_name)s
        WHERE
            user_id = %(user_id)s
        """
        params = user.__dict__
        DatabaseConnection.execute_query(query, params=params)

#Ctrl+Alt+t Ctrl+Alt+l