import time
from colorama import Fore
import views.login as vl
import templates.employee_menu as te
import models.employees as me


# Envia los datos para realizar la marcación de un empleado.
def create_marktime(dni):
    if me.create_marktime(dni):
        print(Fore.GREEN + 'Marcación realizada correctamente.' + Fore.WHITE)
        time.sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al realizar la marcación. Vuelva '
                         'a intentarlo' + Fore.WHITE)
        time.sleep(2.5)

    # Redirección al menú de empleados.
    te.employee_menu(vl.logged_employee)


# Envia los datos necesarios para registrar a un empleado.
def create_employee(employee_info):
    if me.create_employee(employee_info):
        print(Fore.GREEN + 'Empleado registrado correctamente.' + Fore.WHITE)
        time.sleep(1.5)
    else:
        print(Fore.RED + 'Ocurrio un error al registrar al empleado. Vuelva a '
                         'intentarlo' + Fore.WHITE)
        time.sleep(2.5)

    # Redirección al menú de empleados.
    te.employee_menu(vl.logged_employee)
