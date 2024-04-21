from models.employees import get_employee
from templates.employee_menu import employee_menu
import templates.login
import hashlib

# Almacena la información del empleado que inició sesión.
logged_employee = {}


# Retorna un SHA256 hash generado de una cadena.
def hash_password(employee_pass):
    return hashlib.sha256(employee_pass.encode()).hexdigest()


# Formatea la información retornada de la consulta para crear a un empleado.
def format_data_employee(data):
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
    result = get_employee(dni, hash_password(password))

    # Si retorna más de un empleado llama al menú de empleados.
    if len(result):
        employee_menu(format_data_employee(result))
    else:
        # Si no retorna ningun resultado vuelve a mostrar el menú de inicio de
        # sesión.
        templates.login.login_screen(fail=True)
