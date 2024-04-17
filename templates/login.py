from templates.banner import banner
from templates.commons import clean_screen
from templates.mark import mark_menu
from views.login import login_view


# Retorna el DNI y contraseña ingresada por el usuario.
def get_credentials():
    user = input('Ingrese su DNI: ')
    password = input('Ingrese su contraseña: ')
    return user, password


# Menú de inicio de sesión.
def login_menu():
    clean_screen()
    banner()

    # Solicitar credenciales al usuario.
    credentials = get_credentials()

    # Comunicación con view login.
    result = login_view(credentials[0], credentials[1])

    # Acciones a realizar dependiendo de la respuesta de la consulta.
    if isinstance(result, tuple):
        mark_menu(result)
    else:
        print(result)
