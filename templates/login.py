from templates.banner import banner
from templates.commons import clean_screen, decorator
from views.login import login_employee
from colorama import Fore


# Retorna el DNI y la contraseña ingresada por el usuario.
def get_dni_pass():
    dni = input(Fore.WHITE + 'Ingrese su DNI: ')
    password = input(Fore.WHITE + 'Ingrese su contraseña: ')
    decorator()

    # Tratamiento de información ingresada con el usuario:
    # DNI: Solo tiene 8 caracteres y está compuesta de números.
    dni = dni[:8].strip()
    # Contraseña: Solo tiene 4 caracteres y está compuesta de números.
    password = password[:4].strip()

    return dni, password


# Muestra el menú de inicio de sesión.
def login_screen(fail=False):
    clean_screen()
    banner()

    if fail:
        print(Fore.RED + 'DNI o contraseña incorrecta.')
        print('')

    # Solicitar DNI y contraseña al usuario.
    credentials = get_dni_pass()

    # Comunicación con view login.
    login_employee(credentials[0], credentials[1])
