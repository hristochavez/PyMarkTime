from templates.banner import banner
from templates.commons import clean_screen, decorator
from views.login import login_employee
from colorama import Fore
import re


# Validación de DNI.
# DNI: Compuesta de 8 dígitos.
def validate_dni(dni):
    pattern = r'^\d{8}$'
    while not re.match(pattern, dni):
        print(Fore.RED + 'Ingrese un DNI valido. Solo debe de tener 8 '
                         'dígitos.' + Fore.WHITE)
        dni = input('Ingrese su DNI:')

    return dni


# Validación de contraseña.
# Contraseña: Compuesta de 4 dígitos.
def validate_password(password):
    pattern = r'^\d{4}$'
    while not re.match(pattern, password):
        print(Fore.RED + 'Ingrese una contraseña valida. Solo debe de tener 4 '
                   'dígitos.' + Fore.WHITE)
        password = input('Ingrese su contraseña:')

    return password


# Retorna el DNI y la contraseña ingresada por el usuario.
def get_dni_pass():
    dni = input('Ingrese su DNI: ')
    dni = validate_dni(dni)

    password = input('Ingrese su contraseña: ')
    password = validate_password(password)

    return dni, password


# Muestra el menú de inicio de sesión.
def login_screen(fail=False):
    clean_screen()
    banner()

    if fail:
        print(Fore.RED + 'DNI o contraseña incorrecta.' + Fore.WHITE)
        print('')

    # Solicitar DNI y contraseña al usuario.
    credentials = get_dni_pass()

    # Comunicación con view login.
    login_employee(credentials[0], credentials[1])
