from flask import Blueprint

from ..controllers.users_controller import UserController


user_bp = Blueprint('user_bp', __name__) #users

user_bp.route('/login', methods=['POST'])(UserController.login)
user_bp.route('/profile', methods=['GET'])(UserController.show_profile)
# user_bp.route('/<string:username>', methods=['GET'])(UserController.get)
user_bp.route('/logout', methods=['GET'])(UserController.logout)
user_bp.route("/register", methods=['POST'])(UserController.register)
user_bp.route("/welcome", methods=['GET'])(UserController.welcome)
user_bp.route("/update", methods=['POST'])(UserController.update)
# user_bp.route('/', methods=['POST'])(FilmController.create)
# user_bp.route('/<int:film_id>', methods=['PUT'])(FilmController.update)
# user_bp.route('/<int:film_id>', methods=['DELETE'])(FilmController.delete)