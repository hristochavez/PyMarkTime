from models.connection import connect_to_db
from mysql.connector import errors


# Intenta realizar la marcacioń de un empleado.
# Retorna:
# True o False si la marcación se realizó correctamente.
# Una cadena con un mensaje de error en el caso fallar la operación.
def marktime(dni):
    # Indica si la marcación se realizó con exito.
    correct_marking = True

    # Se intenta una conexión con la BBDD.
    connection_result = connect_to_db()

    # Contiene la respuesta luego de intentar una conexión.
    response_message = ''

    # Conexión con la BBDD.
    connection = connection_result[0]

    try:
        cs = connection.cursor()
        stored_proc = 'marktime'
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


# Intenta iniciar la sesión de un empleado.
# Retorna:
# Una tupla que contiene la información del usuario en el caso de que exista,
# una tupla vacia si la consulta no retorna algun empleado y None si se
# enviaron tipos de datos incorrectos al hacer la consulta como por ejemplo
# enviar 7 digitos cuando se ingresa el DNI.
# Una cadena con un mensaje de error en el caso fallar la operación.
def get_employee(dni, password):
    # Contiene una tupla con los datos del usuario que inició sesión.
    result_set = []

    # Se intenta una conexión con el servidor.
    connection_result = connect_to_db()

    # Conexión con la BBDD.
    connection = connection_result

    try:
        cs = connection.cursor()
        stored_proc = 'get_employee'
        parameters = (dni, password)
        cs.callproc(stored_proc, parameters)

        for row in cs.stored_results():
            result_set = row.fetchall()

    except AttributeError as err:
        print(f'Error. Revisar: {err}.')
    except errors.ProgrammingError:
        print('Error al preparar la consulta.')
        cs.close()
        connection.close()
    except errors.DataError:
        print('Formato de datos enviados incorrectos.')
        cs.close()
        connection.close()
    else:
        cs.close()
        connection.close()

    return result_set
