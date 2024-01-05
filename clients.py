from connection import Connection, mysql

class client:

    def addClient(name, surname, age, genre):
        try:
            connect=Connection.connection_db()
            cursor = connect.cursor()

            sql = "INSERT INTO clients (name, surname, age, genre) VALUES (%s, %s, %s, %s)"
            values=(name, surname, age, genre)

            cursor.execute(sql, values)

            connect.commit()
            print("Data inserted successfully")
            connect.close()
        except mysql.connector.Error as err:
            print(f"Error al ingresar los datos a la base de datos: {err}")
