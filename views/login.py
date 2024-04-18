from models.employees import login
import hashlib


# Retorna un SHA256 hash generado de una cadena.
def hash_password(employee_pass):
    return hashlib.sha256(employee_pass.encode()).hexdigest()


# Envia los datos para un inicio de sesión de un empleado.
def init_login(dni, password):
    # Comunicación con el modelo.
    result = login(dni, hash_password(password))

    # Acciones a realizar dependiendo de la respuesta de la consulta.
    if isinstance(result[0], tuple) and len(result[0]) == 0:
        return result[1]
    elif result[0] is None:
        return 'El usuario no existe.'
    else:
        return result[0]
