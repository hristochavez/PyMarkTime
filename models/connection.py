from mysql.connector import connect, Error


def connect_to_db():
    connection = None

    try:
        connection = connect(
            host='localhost',
            user='usr-dev',
            password='Hack2024$$',
            database='pymarktime'
        )
    except Error:
        print('Error al conectarse a la BBDD.')

    return connection

