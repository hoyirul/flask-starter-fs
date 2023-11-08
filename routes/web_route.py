from flask import Blueprint, render_template
from controllers.home_controller import HomeController

homeController = HomeController()
web = Blueprint('web', __name__)

web.add_url_rule('/home', view_func=homeController.index, methods=['GET'])