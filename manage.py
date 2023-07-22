from flask import Flask
import config
from routes import example_route
# import models

@config.app.route('/')
def welcome():
    return '<h2 style="margin: 50px">Welcome to Flask Framework</h2>'

# Register blueprint
config.app.register_blueprint(example_route.example, url_prefix='/api')

if __name__ == '__main__':
    # models.test_connection()
    config.serve()
