from templates.banner import banner
from templates.commons import decorator, qty_chars, clean_screen
from templates.login import login_menu


# Vista a mostrar según elección del usuario.
def show_view(user_opt):
    if user_opt == '1':
        login_menu()


# Retorna la opción seleccionada por el usuario.
def option_selected():
    user_input = input('Elija una opción de la lista: ')

    while user_input not in ['1']:
        user_input = input('Elija una opción valida de la lista: ')

    return user_input


# Vista del menú principal del sistema.
def principal():
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
