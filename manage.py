from flask import Flask
import config
from routes import example_route, user_route, role_route
# import models

@config.app.route('/')
def welcome():
    return '<h2 style="margin: 50px">Welcome to Flask Framework</h2>'

# Register blueprint
config.app.register_blueprint(example_route.example, url_prefix='/api')
config.app.register_blueprint(user_route.user, url_prefix='/api')
config.app.register_blueprint(role_route.role, url_prefix='/api')

if __name__ == '__main__':
    # models.Model().test_connection()
    config.serve()
