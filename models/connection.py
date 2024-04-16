from mysql.connector import connect, Error


def connect_to_db():
    message = ''
    connection = None

    try:
        connection = connect(
            host='localhost',
            user='usr-dev',
            password='Hack2024$$',
            database='marcaciones'
        )
    except Error:
        message = 'Error al conectarse a la base de datos.'
    
    return connection, message

