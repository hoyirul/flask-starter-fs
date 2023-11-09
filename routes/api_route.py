from flask import Blueprint
from controllers.api.example_controller import ExampleController

exampleController = ExampleController()

api = Blueprint('api', __name__)

api.add_url_rule('/examples', view_func=exampleController.index, methods=['GET'])
api.add_url_rule('/examples/<int:id>', view_func=exampleController.show, methods=['GET'])
api.add_url_rule('/examples', view_func=exampleController.store, methods=['POST'])
api.add_url_rule('/examples/<int:id>', view_func=exampleController.update, methods=['PUT'])
api.add_url_rule('/examples/<int:id>', view_func=exampleController.destroy, methods=['DELETE'])