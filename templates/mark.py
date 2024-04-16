from templates.banner import banner
from templates.commons import clean_screen


def option_selected():
    usr_input = input('Ingrese la opción seleccionada.')
    while usr_input not in ['1']:
        usr_input = input('Ingrese una opción válida.')


# Menú de inicio de sesión.
def mark_menu(user):
    clean_screen()
    banner()
    print(f'DNI: {user[0]}')
    print(f'Bienvenido {user[1]}')