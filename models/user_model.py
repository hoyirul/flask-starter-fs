from models import Model
from traits.query_builder import QueryBuilder

class UserModel(Model):
    table = 'users'
    fillable = ['email', 'password', 'role_id']

    def builder(self):
        return QueryBuilder(self)