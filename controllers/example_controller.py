from flask import request
from config.db import connectdb
from models.example_model import ExampleModel
from traits import api_response

exampleModel = ExampleModel()

class ExampleController:

    api = api_response
    
    def index(self):
        try:
            response = exampleModel.findAll(
                columns=['id', 'title', 'description']
            )
            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def store(self):
        try:
            data = request.json
            response = {
                'title': data['title'],
                'description': data['description'],
            }
            
            exampleModel.create((response['title'], response['description']))
            return self.api.success(response, 201)
        except Exception as e:
            return self.api.errors(e, 500)

    def show(self, id):
        try:
            response = exampleModel.findAll(
                columns=['id', 'title', 'description'],
                where=[f'id = {id}']
            )

            if(not response):
                return self.api.success({'message': f'id `{id}` not found!'}, 200)

            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def update(self, id):
        try:
            data = request.json
            response = {
                'title': data['title'],
                'description': data['description'],
            }

            exampleModel.update((response['title'], response['description'], id))
            
            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def destroy(self, id):
        try:
            exampleModel.delete(id)
            return self.api.success('Data deleted successfully!', 200)
        except Exception as e:
            return self.api.errors(e, 500)