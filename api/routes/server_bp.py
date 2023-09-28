from flask import Blueprint
from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp',__name__)

server_bp.route('/', methods = ['POST'])(ServerController.create_server)
server_bp.route('/explore', methods = ['POST'])(ServerController.create_server_explore)
server_bp.route('/', methods = ['GET'])(ServerController.get_servers)
server_bp.route('/serversuser', methods = ['GET'])(ServerController.get_servers_user)
server_bp.route('/count/<int:server_id>', methods=["GET"])(ServerController.get_count)