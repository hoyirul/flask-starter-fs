from flask import jsonify

class ApiResponse:
    def success(self, data, code):
        return jsonify(data), code

    def errors(self, message, code):
        return jsonify({
            'message': 'Error occurred',
            'error': str(message)
        }), code