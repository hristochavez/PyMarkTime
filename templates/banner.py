from templates.commons import decorator, qty_chars


# Banner del sistema.
def banner():
    name_system = 'Sistema PyMarkTime'
    spaces = qty_chars(name_system)
    decorator()
    print('|' + ' ' * spaces + name_system + ' ' * spaces + '|')
    decorator()
