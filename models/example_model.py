from models import Model
from traits.query_builder import QueryBuilder

class ExampleModel(Model):
    table = 'examples'
    fillable = ['title', 'description']

    def builder(self):
        return QueryBuilder(self)