from models.employees import marktime


# Acción a realizar según la opción elegida por el usuario.
def mark_view(dni, option):
    if option == '1':
        marktime(dni)
