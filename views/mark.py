from models.employees import marktime


# Acción a realizar según la opción elegida por el usuario.
def employe_mark(dni, option):
    if option == '1':
        marktime(dni)
