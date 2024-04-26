import re
from colorama import Fore


# Validación de DNI.
# DNI: Compuesto de 8 dígitos.
def dni(dni):
    pattern = r'^\d{8}$'
    while not re.match(pattern, dni):
        print(Fore.RED + 'Ingrese un DNI valido. Solo debe de tener 8 '
                         'dígitos.' + Fore.WHITE)
        dni = input('Ingrese un DNI válido: ')

    return dni


# Validación de contraseña de inicio de sesión.
# Contraseña: Compuesta de 4 dígitos.
def password(password):
    pattern = r'^\d{4}$'
    while not re.match(pattern, password):
        print(Fore.RED + 'Ingrese una contraseña valida. Solo debe de tener 4 '
                         'dígitos.' + Fore.WHITE)
        password = input('Ingrese una contraseña válida: ')

    return password


# Validación del nombre.
# Nombre: Solo debe de tener letras.
def first_name(first_name):
    pattern = r'^[a-zA-Z]+$'
    while not re.match(pattern, first_name):
        print(Fore.RED + 'Ingrese un nombre válido. Solo debe de tener '
                         'letras.' + Fore.WHITE)
        first_name = input('Ingrese un nombre válido: ')

    return first_name


# Valida la respuesta si se deseea deshabilitar a un empleado.
def response_disable(response):
    while response not in ['S', 's', 'n', 'N']:
        response = input('Escriba S o N para inhabilitar al empleado: ')

    return response


# Validación de acción elegida.
def selected_action(qty_actions, selected_action):
    # Cantidad de acciones permitidas.
    qty_actions = [str(x) for x in range(1, qty_actions + 1)]

    while selected_action not in qty_actions:
        selected_action = input('Elija el número de acción a realizar: ')

    return selected_action
