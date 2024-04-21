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
