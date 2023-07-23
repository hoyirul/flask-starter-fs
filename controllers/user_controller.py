from flask import request
from models.user_model import UserModel
from traits.api_response import ApiResponse

userModel = UserModel()

class UserController:

    api = ApiResponse()
    
    def index(self):
        try:
            response = userModel.builder().select(['users.id', 'users.email', 'users.password', 'roles.role']).join('roles', 'users.role_id = roles.id').get()

            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def store(self):
        try:
            req = request.json
            data = {
                'email': f"'{req['email']}'",
                'password': f"'{req['password']}'",
            }

            query = userModel.builder().insert(data).build()
            userModel.execute(query)

            return self.api.success(data, 201)
        except Exception as e:
            return self.api.errors(e, 500)

    def show(self, id):
        try:
            response = userModel.builder().select(['users.id', 'users.email', 'users.password', 'roles.role']).join('roles', 'users.role_id = roles.id').where('users.id', '=', id).first()

            if not response:
                return self.api.success({'message': f'id `{id}` not found!'}, 200)

            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)