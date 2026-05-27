from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
# Create your views here.



# TODO:
# LIMITAR FUNCIONES SEGUN TIPO DE EMPLEADO
# VISTA (Empleado): REPARTIDOR - COCINA: PARA VER PEDIDOS
# - Modificar pedido

# VISTA (Manager): Gestionar empleados, productos y men


def is_manager(user):
    return user.role == "manager"
    
def is_employee(user):
    return user.role in ['delivery_man', 'employee']


@user_passes_test(is_manager)
def manager_dashboard(request):
    return render(request, 'url')

@user_passes_test(is_employee)
def orders_dahsboard(request):
    return render(request, 'url') 

        