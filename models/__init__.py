from config.db import Database

db = Database()
class Model:

    def test_connection(self):
        try:
            connection = db.connectdb()
            if connection.is_connected():
                print('Database connection successful.')
                connection.close()
            else:
                print('Database connection failed.')
        except Exception as e:
            print('Error:', str(e))

    def fetchall(self, query):
        connection = db.connectdb()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        response = cursor.fetchall()
        cursor.close()
        connection.close()
        return response

    def fetchone(self, query):
        connection = db.connectdb()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        response = cursor.fetchone()
        cursor.close()
        connection.close()
        return response
    
    def execute(cls, query):
        connection = db.connectdb()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    