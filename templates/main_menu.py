from templates.banner import banner
from templates.commons import decorator, qty_chars, clean_screen
from templates.login import login_screen


# Vista a mostrar según elección del usuario.
def show_menu(usr_opt):
    if usr_opt == '1':
        login_screen()


# Retorna la opción seleccionada por el usuario.
def get_option_selected():
    usr_input = input('Elija una opción de la lista: ')

    while usr_input not in ['1']:
        usr_input = input('Elija una opción valida de la lista: ')

    return usr_input


# Menú principal del sistema.
def principal_menu():
    clean_screen()
    banner()

    opt_1 = 'Presione 1 para marcar.'
    spaces = qty_chars(opt_1)
    print('|' + ' ' * spaces + opt_1 + ' ' * spaces + '|')

    opt_2 = 'Presione 2 para registrar a un empleado (PROXIMAMENTE).'
    spaces = qty_chars(opt_2)
    print('|' + ' ' * spaces + opt_2 + ' ' * spaces + '|')

    opt_3 = 'Presione 3 para eliminar a un empleado (PROXIMAMENTE).'
    spaces = qty_chars(opt_3)
    print('|' + ' ' * spaces + opt_3 + ' ' * spaces + '|')

    opt_4 = 'Presione 4 para actualizar a un empleado (PROXIMAMENTE).'
    spaces = qty_chars(opt_4)
    print('|' + ' ' * spaces + opt_4 + ' ' * spaces + '|')

    decorator()
