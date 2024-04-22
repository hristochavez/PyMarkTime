import re
from colorama import Fore
from templates.banner import banner
from templates.commons import clean_screen
from views.actions import create_marktime, create_employee

# Permisos que puede tener un empleado:
# 1 -> puede marcar.
# 2 -> puede registrar empleados.
# 3 -> puede inhabilitar empleados.
actions = {
    1: 'Realizar marcación.',
    2: 'Registrar a un empleado.',
    3: 'Inhabilitar a un empleado.'
}


# Validación de DNI.
# DNI: Compuesta de 8 dígitos.
def validate_dni(dni):
    pattern = r'^\d{8}$'
    while not re.match(pattern, dni):
        print(Fore.RED + 'Ingrese un DNI valido. Solo debe de tener 8 '
                         'dígitos.' + Fore.WHITE)
        dni = input('Ingrese su DNI:')

    return dni

# Validación del nombre.
# Nombre: Solo debe de tener letras.
def validate_first_name(first_name):
    pattern = r'^[a-zA-Z]+$'
    while not re.match(pattern, first_name):
        print(Fore.RED + 'Ingrese un nombre válido. Solo debe de tener '
                         'letras.' + Fore.WHITE)
        first_name = input('Ingrese su nombre:')

    return first_name


# Recoge la información necesaria para crear a un empleado.
def new_employee():
    dni = input('Ingrese el DNI del empleado (8 caracteres): ')
    dni = validate_dni(dni)

    first_name = input('Ingrese el nombre del empleado (solo debe contener '
                       'letras): ')

    first_name = validate_first_name(first_name)

    # Formatea la información del nuevo empleado.
    employee = {
        'dni': dni,
        'first_name': first_name
    }

    return employee


# Retorna una lista de acciones que puede realizar un usuario donde cada
# acciónn es una tupla conformada por:
# (número de opción a mostrar, llave, valor).
def get_actions(permissions):
    # Lista de acciones permitidas.
    permitted_actions = []

    # Llenar la lista de acciones permitidas de acuerdo a los permisos que
    # tiene el usuario.
    num_opt = 1
    for key, value in actions.items():
        if key in permissions:
            permitted_actions.append((num_opt, key, value))
            num_opt += 1

    return permitted_actions


# Ejecuta la acción elegida por el usuario.
# Obtiene la acción a realizar de la lista de acciones que puede realizar
# el usuario.
def action_to_do(employee_actions, selected_action, dni=None):
    do = 0

    for action in employee_actions:
        if str(action[0]) == selected_action:
            do = action[1]
            break

    if do == 1:
        create_marktime(dni)
    elif do == 2:
        create_employee(new_employee())


# Muestra el meńu principal del empleado.
def employee_menu(employee):
    clean_screen()
    banner()

    print(f'DNI: {employee["dni"]}')
    print(f'Bienvenido(a) {employee["first_name"]}')
    print('')

    # Muestra los permisos que tiene el usuario.
    print('Usted tiene los siguientes permisos:')
    employee_actions = get_actions(employee['permissions'])

    for action in employee_actions:
        print(f'{action[0]}.- {action[2]}')

    # Pregunta al usuario por la acción a realizar.
    valid_actions = [str(x) for x in range(1, len(employee_actions) + 1)]
    print('')
    selected_action = input('Elija el número de acción a realizar: ')

    while selected_action not in valid_actions:
        selected_action = input('Elija el número de acción a realizar: ')

    # Realiza la acción seleccionada por el usuario.
    action_to_do(employee_actions, selected_action, employee['dni'])