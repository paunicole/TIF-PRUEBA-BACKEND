from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class UserNotFound(Exception):
    def __init__(self, status_code, name = "User Not Found/Exists", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = 404

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class UsernameExists(Exception):
    def __init__(self, status_code, name = "User Exists", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = 404

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
    def serialize(self):
        return {    "status_code" : self.status_code,
                    "name": self.name,
                    "description": self.description,
        }
    