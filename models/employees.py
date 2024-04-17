from models.connection import connect_to_db
from mysql.connector import errors


# Crea un registro que representa la marcación de un usuario.
def marktime(dni):
    correct_marking = True

    # Se intenta una conexión con el servidor.
    connection_result = connect_to_db()

    # Contiene la respuesta luego de intentar una conexión.
    response_message = ''

    # Conexión con la BBDD.
    connection = connection_result[0]

    try:
        cs = connection.cursor()
        stored_proc = 'mark'
        parameters = (dni, )
        cs.callproc(stored_proc, parameters)
        connection.commit()
    except AttributeError:
        response_message = connection_result[1]
    except errors.IntegrityError:
        response_message = 'El empleado no existe. No se puede realizar marca.'
    except errors.ProgrammingError:
        response_message = 'Error al preparar la consulta.'
        cs.close()
        connection.close()
    except errors.DataError:
        response_message = 'DNI o contraseña incorrecta.'
        cs.close()
        connection.close()
    else:
        cs.close()
        connection.close()

    return correct_marking, response_message


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
