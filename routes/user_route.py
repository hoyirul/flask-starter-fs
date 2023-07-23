from flask import Blueprint
from controllers.user_controller import UserController

userController = UserController()
user = Blueprint('user', __name__)

user.add_url_rule('/users', view_func=userController.index, methods=['GET'])
user.add_url_rule('/users/<int:id>', view_func=userController.show, methods=['GET'])
user.add_url_rule('/users', view_func=userController.store, methods=['POST'])