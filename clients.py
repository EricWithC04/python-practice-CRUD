from connection import Connection, mysql

class client:

    def showClients():
        try:
            connect=Connection.connection_db()
            cursor = connect.cursor()

            cursor.execute("SELECT * FROM clients")
            all_clients = cursor.fetchall()

            connect.commit()
            connect.close()

            return all_clients
        except mysql.connector.Error as err:
            print(f"Error al mostrar los datos: {err}")

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

    def updateClient(name, surname, age, genre):
        try:
            connect=Connection.connection_db()
            cursor = connect.cursor()

            sql = "UPDATE clients SET clients.name = %s, clients.surname = %s, clients.age = %s, clients.genre = %s WHERE clients.name = %s AND clients.surname = %s"
            values=(name, surname, age, genre, name, surname)

            cursor.execute(sql, values)

            connect.commit()
            print("Data updated successfully")
            connect.close()
        except mysql.connector.Error as err:
            print(f"Error al ingresar los datos a la base de datos: {err}")