from templates.banner import banner
from templates.commons import clean_screen
from templates.mark import mark_menu
from views.login import init_login


# Retorna el DNI y la contraseña ingresada por el usuario.
def get_dni_pass():
    dni = input('Ingrese su DNI: ')
    password = input('Ingrese su contraseña: ')
    return dni, password


# Muestra el menú de inicio de sesión.
def login_menu():
    clean_screen()
    banner()

    # Solicitar DNI y contraseña al usuario.
    credentials = get_dni_pass()

    # Comunicación con view login.
    result = init_login(credentials[0], credentials[1])

    # Acciones a realizar dependiendo de la respuesta de la consulta.
    if isinstance(result, tuple):
        mark_menu(result)
    else:
        print(result)
