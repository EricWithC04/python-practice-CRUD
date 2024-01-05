import mysql.connector

class Connection:
    def connection_db():
        try:
            db = mysql.connector.connect(
                user="root",
                password="",
                port=3306,
                host="localhost",
                database="pythondb"
            )
            print("Succesfully connected to database")

            return db
        except mysql.connector.Error as err:
            print(f"Error al conectarse a la base de datos {err}")
    
    connection_db()