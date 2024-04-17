from templates.banner import banner
from templates.commons import clean_screen


# Menú de inicio de sesión.
def mark_menu(user):
    clean_screen()
    banner()
    print(f'DNI: {user[0]}')
    print(f'Bienvenido {user[1]}')
