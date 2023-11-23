from flask import Blueprint
from traits import render, view
from controllers.web.test_controller import TestController

testController = TestController()
test = Blueprint('test', __name__)

test.add_url_rule('/', view_func=testController.index, methods=['GET'])