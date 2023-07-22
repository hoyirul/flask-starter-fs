import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

def check_secret_key():
    secret_key = os.getenv('SECRET_KEY')
    if secret_key:
        return True
    else:
        return False

def serve():
    if check_secret_key() == False:
        print('you have not generated a key, please generate a key with `python3 config/generate_key.py`')
    else:
        app.run(
            host='0.0.0.0', 
            port=os.getenv('APP_PORT'),
            debug=True if os.getenv('APP_DEBUG') == 'development' else False
        )