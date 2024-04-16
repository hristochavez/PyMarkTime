from models.connection import connect_to_db
from mysql.connector import errors, cursor


def login(user, password):
    # Contiene una tupla con los datos del usuario que inició sesión.
    result = ()

    # Se intenta una conexión con el servidor.
    connection_response = connect_to_db()

    # Contiene la respuesta luego de intentar una conexión.
    message = connection_response[1]

    try:
        curs = connection_response[0].cursor()
        stored_proc = 'login_employee'
        parameters = (user, password)
        curs.callproc(stored_proc, parameters)

        for row in curs.stored_results():
            result = row.fetchone()
    except AttributeError:
        message = connection_response[1]
    except errors.ProgrammingError:
        message = 'Error al preparar la consulta.'
        curs.close()
        connection_response[0].close()
    except errors.DataError:
        message = 'DNI o contraseña incorrecta.'
        curs.close()
        connection_response[0].close()
    else:
        curs.close()
        connection_response[0].close()

    return result, message
