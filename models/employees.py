from models.connection import connect_to_db
from mysql.connector import errors


# Intenta realizar la marcacioń de un empleado.
# Retorna:
# True o False si la marcación se realizó correctamente.
# Una cadena con un mensaje de error en el caso fallar la operación.
def create_marktime(dni):
    # Indica si la marcación se realizó con exito.
    success_marking = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'create_marktime'
        parameters = (dni, )
        cs.callproc(stored_proc, parameters)
        connection.commit()
    except AttributeError as err:
        print(f'Ocurio un error. Revisar: {err}.')
    except errors.IntegrityError:
        success_marking = False
        connection.rollback()
    except errors.ProgrammingError:
        print('¿Existe el procedimiento almacenado?')
        cs.close()
        connection.close()
    except errors.DataError:
        print('¿Ha sido la data formateada correctamente para realizar la '
              'operación?')
        cs.close()
        connection.close()
    else:
        cs.close()
        connection.close()

    return success_marking


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


# Crear a un empleado.
def create_employee(new_employee):
    # Indica si la marcación se realizó con exito.
    success_create = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'create_employee'
        parameters = (new_employee['dni'], new_employee['first_name'])
        cs.callproc(stored_proc, parameters)
        connection.commit()
    except AttributeError as err:
        print(f'Ocurio un error. Revisar: {err}.')
    except errors.IntegrityError:
        success_create = False
        connection.rollback()
    except errors.ProgrammingError:
        print('¿Existe el procedimiento almacenado?')
        cs.close()
        connection.close()
    except errors.DataError:
        print('¿Ha sido la data formateada correctamente para realizar la operación?')
        cs.close()
        connection.close()
    else:
        cs.close()
        connection.close()

    return success_create


# Obtiene la información del empleado consultado.
def employee_information(dni):
    result_set = ()

    # Se intenta una conexión con el servidor.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'employee_information'
        parameters = (dni,)
        cs.callproc(stored_proc, parameters)

        for row in cs.stored_results():
            result_set = row.fetchone()
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


# Inhabilita a un empleado.
def disable_employee(dni_employee_to_disable, dni):
    # Indica si la inhabilitación se realizó con exito.
    success_disabled = True

    # Se intenta una conexión con la BBDD.
    connection = connect_to_db()

    try:
        cs = connection.cursor()
        stored_proc = 'disable_employee'
        parameters = (dni_employee_to_disable, dni)
        cs.callproc(stored_proc, parameters)
        connection.commit()
    except AttributeError as err:
        print(f'Ocurio un error. Revisar: {err}.')
    except errors.IntegrityError:
        success_disabled = False
        connection.rollback()
    except errors.ProgrammingError:
        print('¿Existe el procedimiento almacenado?')
        cs.close()
        connection.close()
    except errors.DataError:
        print('¿Ha sido la data formateada correctamente para realizar la '
              'operación?')
        cs.close()
        connection.close()
    else:
        cs.close()
        connection.close()

    return success_disabled
