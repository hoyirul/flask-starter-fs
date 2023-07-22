class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self.columns = ['*']
        self.where_conditions = []
        self.order_by = None
        self.group_by = None
        self.join_tables = []

    def select(self, columns):
        self.columns = columns
        return self

    def where(self, conditions):
        self.where_conditions.extend(conditions)
        return self

    def order_by(self, column):
        self.order_by = column
        return self

    def group_by(self, column):
        self.group_by = column
        return self

    def join(self, table, on_condition):
        self.join_tables.append((table, on_condition))
        return self

    def build(self):
        query = f'SELECT {", ".join(self.columns)} FROM {self.table}'

        if self.join_tables:
            for join_table, on_condition in self.join_tables:
                query += f' INNER JOIN {join_table} ON {on_condition}'

        if self.where_conditions:
            where_clause = " AND ".join(self.where_conditions)
            query += f' WHERE {where_clause}'

        if self.order_by:
            query += f' ORDER BY {self.order_by}'

        if self.group_by:
            query += f' GROUP BY {self.group_by}'

        return query
