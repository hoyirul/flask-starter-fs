from models import Model
from traits.query_builder import QueryBuilder

class ExampleModel(Model):
    table = 'examples'

    def findAll(self, columns=None, where=None, order_by=None, group_by=None):
        query_builder = QueryBuilder(self.table)

        if columns:
            query_builder.select(columns)

        if where:
            query_builder.where(where)

        if order_by:
            query_builder.order_by(order_by)

        if group_by:
            query_builder.group_by(group_by)

        query = query_builder.build()
        results = self.fetchall(query)

        if len(results) == 1:
            return self.fetchone(query)
        
        return results

    def create(self, data):
        query = f'INSERT INTO {self.table} VALUES(null, %s, %s, null, null)'
        return self.commit(query, (data))

    def update(self, data):
        query = f'UPDATE {self.table} SET title = %s , description = %s WHERE id = %s'
        return self.commit(query, (data))

    def delete(self, id):
        query = f'DELETE FROM {self.table} WHERE id = %s'
        return self.commit(query, (id,))