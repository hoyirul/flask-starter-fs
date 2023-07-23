from models import Model
from traits.query_builder import QueryBuilder

class RoleModel(Model):
    table = 'roles'
    fillable = ['role']

    def builder(self):
        return QueryBuilder(self)