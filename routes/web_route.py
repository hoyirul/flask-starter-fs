from flask import Blueprint
from traits import render, view
from controllers.web.home_controller import HomeController


homeController = HomeController()
web = Blueprint('web', __name__)

def welcome():
    data = {
        'title': 'Welcome to Flask',
        'docs': 'https://github.com/hoyirul/flask-starter-fs',
        'github': 'https://github.com/hoyirul/flask-starter-fs',
        'powered': 'https://flask.palletsprojects.com/en/3.0.x/'
    }
    
    return render(view('welcome'), data=data)

web.add_url_rule('/', view_func=welcome, methods=['GET'])

web.add_url_rule('/home', view_func=homeController.index, methods=['GET'])
web.add_url_rule('/plot2d', view_func=homeController.plot2d, methods=['GET'])
web.add_url_rule('/plot3d', view_func=homeController.plot3d, methods=['GET'])