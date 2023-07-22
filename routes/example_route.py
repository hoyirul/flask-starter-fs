from flask import Blueprint
from controllers.example_controller import ExampleController
from config import app

exampleController = ExampleController()
example = Blueprint('example', __name__)

example.add_url_rule('/examples', view_func=exampleController.index, methods=['GET'])
example.add_url_rule('/examples/<int:id>', view_func=exampleController.show, methods=['GET'])
example.add_url_rule('/examples', view_func=exampleController.store, methods=['POST'])
example.add_url_rule('/examples/<int:id>', view_func=exampleController.update, methods=['PUT'])
example.add_url_rule('/examples/<int:id>', view_func=exampleController.destroy, methods=['DELETE'])