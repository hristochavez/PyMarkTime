from templates.principal_menu import principal_menu, get_option_selected, show_menu


# Menu principal del sistema.
principal_menu()

# Opción seleccionada por el usuario.
user_opt = get_option_selected()

# Vista mostrar según la opción seleccionada por el usuario.
show_menu(user_opt)
