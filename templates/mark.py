from templates.banner import banner
from templates.commons import clean_screen
from views.mark import employe_mark


# Retorna la opción elegida por el usuario.
def option_selected():
    usr_input = input('Ingrese la opción seleccionada: ')
    while usr_input not in ['1']:
        usr_input = input('Ingrese una opción válida: ')

    return usr_input


# Menú para hacer una marcación.
def mark_menu(employee):
    clean_screen()
    banner()

    dni = employee[0]
    name_employee = employee[1]

    print(f'DNI: {dni}')
    print(f'Bienvenido {name_employee}')
    usr_input = option_selected()
    employe_mark(employee[0], usr_input)
