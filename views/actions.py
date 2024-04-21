import time
import views.login as vl
import templates.employee_menu as te
import models.employees as me


# Envia los datos para realizar la marcación de un empleado.
def create_marktime(dni):
    if me.create_marktime(dni):
        print('Marcación realizada correctamente.')
    else:
        print('Ocurrio un error al realizar la marcación.')
    time.sleep(1)

    # Redirección al menú de empleados.
    te.employee_menu(vl.logged_employee)


# Envia los datos necesarios para registrar a un empleado.
def create_employee(employee_info):
    if me.create_employee(employee_info):
        print('Empleado creado correctamente.')
        time.sleep(1)
    else:
        print('Ocurrio un error al realizar la creación. Vuelva a intentarlo.')
        time.sleep(2)

    # Redirección al menú de empleados.
    te.employee_menu(vl.logged_employee)
