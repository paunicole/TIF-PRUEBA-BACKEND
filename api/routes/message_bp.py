from flask import Blueprint
from ..controllers.message_controller import MessageController

message_bp = Blueprint('message_bp',__name__)

message_bp.route('/', methods = ['POST'])(MessageController.create_message)
message_bp.route('/<int:message_id>/<message>', methods = ['PUT'])(MessageController.update_message)
message_bp.route('/', methods = ['GET'])(MessageController.get_messages)
#message_bp.route('/<int:message_id>', methods = ['GET'])(MessageController.get_message)
message_bp.route('/<int:message_id>', methods = ['DELETE'])(MessageController.delete_message)
#esperamo recibir un entero es el id del mensaje 
message_bp.route('/delete/<int:idMensaje>', methods = ['DELETE'])(MessageController.eliminarMensaje)