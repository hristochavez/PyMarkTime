from templates.banner import banner
from templates.commons import clean_screen
from views.mark import mark_view


# Retorna la opción elegida por el usuario.
def option_selected():
    usr_input = input('Ingrese la opción seleccionada: ')
    while usr_input not in ['1']:
        usr_input = input('Ingrese una opción válida: ')

    return usr_input


# Menú de inicio de sesión.
def mark_menu(user):
    clean_screen()
    banner()
    print(f'DNI: {user[0]}')
    print(f'Bienvenido {user[1]}')
    usr_input = option_selected()
    mark_view(user[0], usr_input)
