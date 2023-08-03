from flask import Blueprint
from controllers.role_controller import RoleController

roleController = RoleController()
role = Blueprint('role', __name__)

role.add_url_rule('/find_with_order_by', view_func=roleController.find_with_order_by, methods=['GET'])
role.add_url_rule('/find_with_group_by', view_func=roleController.find_with_group_by, methods=['GET'])
role.add_url_rule('/find_with_or_where', view_func=roleController.find_with_or_where, methods=['GET'])
role.add_url_rule('/find_with_and_where', view_func=roleController.find_with_and_where, methods=['GET'])
# role.add_url_rule('/roles/<int:id>', view_func=roleController.find_with_group_by, methods=['GET'])