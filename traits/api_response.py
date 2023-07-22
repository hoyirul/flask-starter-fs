from flask import jsonify

def success(data, code):
    return jsonify(data), code

def errors(message, code):
    return jsonify({
        'message': 'Error occurred',
        'error': str(message)
    }), code