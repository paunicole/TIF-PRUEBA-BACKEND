from ..models.users_model import User 
from ..models.exceptions import UserNotFound,UsernameExists
from flask import request,session
import datetime as dt

class UserController:
    @classmethod
    def login(cls):
        """del login trae un objeto json"""
        data = request.json
        # print("Desde login_controller",data)
        user = User(
            username = data.get('username'),
            password = data.get('password')
        )
        
        #comprueba si existe el usuario, por el nombre y la contraseña
        if User.is_registered(user):
            session['username'] = data.get('username')#guarda el nombre_de usuario
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    @classmethod
    def show_profile(cls):
        """va y busca al usuario y trae sus datos"""
        username = session.get('username')
        user = User.get(User(username = username))
        # print("Desde show_profile",user.serialize())

        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
        
    @classmethod
    def welcome(cls):
        username = session.get('username')
        user = User.get(User(username = username))
        print("Desde welcome",user.serialize())
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
        
    @classmethod
    def logout(cls):
        """cierra a session"""
        session.pop('username', None)#se elimina el usuario, o bien se le cambia el valor a none
        return {"message": "Sesion cerrada"}, 200
    
    @classmethod
    def get(cls, username):
        """Get a film by id"""
        user = User(username=username)
        result = User.get(user)

        if result is not None:
            return result
        else:
            raise UserNotFound("usuario no encontrado")
    
    @classmethod
    def register(cls):
        data=request.json
        print("Json desde Formulario--->",data)
        
        if "birthdate" in data:
            fecha_nac= str(data.get("birthdate")) #2000-02-10 (año, mes , dia)
        
            print(fecha_nac) #por defecto ---> Año-Mes-Dia
            if fecha_nac == "":
                data["birthdate"]=None
                #print(type(fecha_nac))#<class 'datetime.datetime'>
            else:
                fecha_nac= dt.datetime.fromisoformat(fecha_nac)
                data["birthdate"]=fecha_nac
        user=User(**data)
        print("\nUser:",user.serialize())

        if User.createUser(user) is None:
            # raise UsernameExists("Este user ya existe!!")
            return {"message":UsernameExists("Este user ya existe!!").serialize()},400
        else:
            return {"message":"todo en orden"},200
           
    @classmethod
    def update(cls):
        data=request.json
        user=User(**data)
        print("Desde udate--------->",user)
        User.updateUser(user)
        return {"message":"Id actualizao"},200