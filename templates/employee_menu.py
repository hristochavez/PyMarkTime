from templates.banner import banner
from templates.commons import clean_screen

# Permisos que puede tener un empleado:
# 1 -> puede marcar.
# 2 -> puede registrar empleados.
# 3 -> puede actualizar empleados.
# 4 -> puede inhabilitar empleados.
actions = {
    1: 'Realizar una marcación.',
    2: 'Registrar a un empleado.',
    3: 'Actualizar a un empleado.',
    4: 'Inhabilitar a un empleado.'
}


# Retorna una lista de acciones que puede realizar un usuario.
def get_actions(permissions):
    # Lista de acciones permitidas.
    permitted_actions = []

    # Llenar la lista de acciones permitidas de acuerdo a los permisos que
    # tiene el usuario.
    i = 1
    for key, value in actions.items():
        if key in permissions:
            permitted_actions.append((i, key, value))
            i += 1

    return permitted_actions


# Muestra el meńu principal del empleado.
def employee_menu(employee):
    clean_screen()
    banner()

    print(f'DNI: {employee["dni"]}')
    print(f'Bienvenido(a) {employee["first_name"]}')
    print('')

    print('Elija la acción a realizar:')
    actions = get_actions(employee['permissions'])

    for action in actions:
        print(f'{action[0]}.- {action[2]}')

    print('')
    selected_action = input('Elija el número de acción a realizar: ')

    valid_actions = [str(x) for x in range(1, len(actions) + 1)]

    while selected_action not in valid_actions:
        selected_action = input('Elija el número de acción a realizar: ')
