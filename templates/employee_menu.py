import re
import time
import views.actions as va
import views.login as vl
from colorama import Fore
from templates.banner import banner
from templates.commons import clean_screen


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


# Procesa la inhabilitación de un empleado.
def disable_employee(result, dni_employee_to_disable, dni):
    if result is None:
        print(Fore.RED, end='')
        print(f'El empleado con DNI {dni_employee_to_disable} no existe.')
        print(Fore.WHITE, end='')
        time.sleep(2.5)
    elif result[1] == 0:
        print(Fore.RED, end='')
        print(f'El empleado {result[0]} con DNI {dni_employee_to_disable}'
              ' ya se encuentra inhabilitado.')
        print(Fore.WHITE, end='')
        time.sleep(2.5)
    elif result[1] == 1:
        print(Fore.YELLOW, end='')
        disable_emp = input(f'¿Desea inhabilitar al empleado {result[0]} con '
                            'DNI {dni_employee_to_disable}? Escriba S o N: ')
        print(Fore.WHITE, end='')

        while disable_emp not in ['S', 's', 'n', 'N']:
            disable_emp = input('Escriba S o N para inhabilitar al empleado.')

        if disable_emp == 's' or disable_emp == 'S':
            va.disable_employee(dni_employee_to_disable, dni)

    employee_menu(vl.logged_employee)


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
        va.create_marktime(dni)
    elif do == 2:
        va.create_employee(new_employee())
    elif do == 3:
        # Solicita el dni del empleado a inhabilitar.
        dni_employee_to_disable = input('Ingrese el DNI del empleado'
                                        ' (8 caracteres): ')
        dni_employee_to_disable = validate_dni(dni_employee_to_disable)

        # Resultado de la solicitud de la información del empleado.
        result = va.employee_information(dni_employee_to_disable)

        # Inhabilitación del empleado.
        disable_employee(result, dni_employee_to_disable, dni)


# Retorna una lista de acciones que puede realizar un usuario donde cada
# acciónn es una tupla conformada por:
# (número de opción a mostrar, llave de la acción, descripción de la acción).
def get_actions(permissions):
    # Lista de acciones permitidas.
    permitted_actions = []

    # Llena la lista de acciones permitidas de acuerdo a los permisos que
    # tiene el usuario.
    num_opt = 1
    for key, value in actions.items():
        if key in permissions:
            permitted_actions.append((num_opt, key, value))
            num_opt += 1

    return permitted_actions


# Muestra el meńu principal del empleado.
def employee_menu(employee):
    clean_screen()
    banner()

    print(f'DNI: {employee["dni"]}')
    print(f'Bienvenido(a) {employee["first_name"]}')
    print('')

    # Muestra los permisos que tiene el usuario.
    print('Usted tiene los siguientes permisos:')
    # employee['permissions'] contiene una tupla con los id de los permisos
    # que tiene el usuario.
    employee_actions = get_actions(employee['permissions'])
    for action in employee_actions:
        print(f'{action[0]}.- {action[2]}')

    # Pregunta al usuario por la acción a realizar.
    # Cantidad de acciones permitidas.
    qty_actions = [str(x) for x in range(1, len(employee_actions) + 1)]

    print('')
    selected_action = input('Elija el número de acción a realizar: ')
    while selected_action not in qty_actions:
        selected_action = input('Elija el número de acción a realizar: ')

    # Realiza la acción seleccionada por el usuario.
    action_to_do(employee_actions, selected_action, employee['dni'])
