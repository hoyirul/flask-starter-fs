from flask import request
from models.role_model import RoleModel
from models.user_model import UserModel
from traits.api_response import ApiResponse

roleModel = RoleModel()

class RoleController:

    api = ApiResponse()
    
    def find_with_order_by(self):
        try:
            response = roleModel.builder().select(['id', 'role']).order_by('id', 'desc').get()
  
            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)

    def find_with_group_by(self):
        try:
            response = roleModel.builder().select(['id', 'role']).group_by(['id', 'role']).get()
            
            return self.api.success(response, 200)
        except Exception as e:
            return self.api.errors(e, 500)