from config.db import connectdb

class Model:
    def test_connection(self):
        try:
            connection = connectdb()
            if connection.is_connected():
                print('Database connection successful.')
                connection.close()
            else:
                print('Database connection failed.')
        except Exception as e:
            print('Error:', str(e))

    def fetchall(self, query):
        connection = connectdb()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        response = cursor.fetchall()
        cursor.close()
        connection.close()
        return response

    def fetchone(self, query):
        connection = connectdb()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        response = cursor.fetchone()
        cursor.close()
        connection.close()
        return response
    
    def execute(cls, query):
        connection = connectdb()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    