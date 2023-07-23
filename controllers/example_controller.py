from flask import request
from models.example_model import ExampleModel
from traits.api_response import ApiResponse

exampleModel = ExampleModel()

class ExampleController:

    api = ApiResponse()
    
    def index(self):
        try:
            response = exampleModel.builder().select(['id', 'title', 'description']).get()

            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def store(self):
        try:
            req = request.json
            data = {
                'title': f"'{req['title']}'",
                'description': f"'{req['description']}'",
            }

            query = exampleModel.builder().insert(data).build()
            exampleModel.execute(query)

            return self.api.success(data, 201)
        except Exception as e:
            return self.api.errors(e, 500)

    def show(self, id):
        try:
            response = exampleModel.builder().where('id', '=', id).first()

            if not response:
                return self.api.success({'message': f'id `{id}` not found!'}, 200)

            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def update(self, id):
        try:
            req = request.json
            data = {
                'title': f"'{req['title']}'",
                'description': f"'{req['description']}'",
            }
            query = exampleModel.builder().where('id', '=', id).update(data).build()
            exampleModel.execute(query)

            return self.api.success(data, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def destroy(self, id):
        try:
            query = exampleModel.builder().where('id', '=', id).delete().build()
            exampleModel.execute(query)

            return self.api.success(f'Data with id `{id}` deleted successfully!', 200)
        except Exception as e:
            return self.api.errors(e, 500)