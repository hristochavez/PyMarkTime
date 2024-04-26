import hashlib
import templates.login as tl
import templates.employee_menu as tem
from models.employees import get_employee

# Almacena la información del empleado que inició sesión.
logged_employee = {}


# Retorna un SHA256 hash generado de una cadena.
def hash_password(employee_pass):
    return hashlib.sha256(employee_pass.encode()).hexdigest()


# Formatea la información retornada de la consulta para crear a un empleado.
def format_employee(data):
    dni = data[0][0]
    first_name = data[0][1]
    permissions = []
    for row in data:
        permissions.append(row[2])

    employee = {
        'dni': dni,
        'first_name': first_name,
        'permissions': permissions
    }

    global logged_employee
    logged_employee = employee

    return employee


# Envia los datos para un inicio de sesión de un empleado.
def login_employee(dni, password):
    # Comunicación con el modelo.
    query_result = get_employee(dni, hash_password(password))

    # Si retorna a un empleado, invoca al menú de empleados.
    if len(query_result):
        tem.menu(format_employee(query_result))
    else:
        # Si no retorna ningun resultado vuelve a mostrar el menú de inicio de
        # sesión.
        tl.login_screen(fail=True)
