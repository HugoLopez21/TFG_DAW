from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import EmployeeChangeForm, EmployeeCreationForm
# Create your views here.



# TODO:
# LIMITAR FUNCIONES SEGUN TIPO DE EMPLEADO
# VISTA (Empleado): REPARTIDOR - COCINA: PARA VER PEDIDOS
# - Modificar pedido

# VISTA (Manager): Gestionar empleados, productos y men



# COMPROBACIONES DE USUARIOS
def is_manager(user):
    return user.role == "manager"
    
def is_employee(user):
    return user.role in ['delivery_man', 'employee']


# RENDERIZA TEMPLATE DE LOS EMPLEADOS
# Devolver la lista de usuarios empleados
# Devolver la lista de productos filtrarlos para saber si estan en la carta o no

@user_passes_test(is_employee)
def orders_dahsboard(request):
    return render(request, 'url') 



# RENDERIZA DASHBOAR DEL MANAGER
@user_passes_test(is_manager)
def manager_dashboard(request):
    return render(request, 'url')



@user_passes_test(is_manager)
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado creado con éxito.")
            return redirect() # URL
    else:
        form = EmployeeCreationForm()
    return render() # URL plantilla

@user_passes_test(is_manager)
def delete_employee(request, employee_id):
    user = get_object_or_404(get_user_model(), id=employee_id)
    
    if is_manager(user):
        user.delete()
        messages.error(request, "No puedes eliminar al manager.")
    else:
        user.delete()
        messages.success(request, "Usuario eliminado con éxito.")
        
    return redirect() # añadir nombre url o vista

@user_passes_test(is_manager)
def modify_employee(request, employee_id):
    user = get_object_or_404(get_user_model(), id=employee_id)
    
    if request.method == 'POST':
        form = EmployeeChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado modificado con éxito.")
            return redirect('panel_principal')
    else:
        form = EmployeeChangeForm(instance=user)
        
    return render() #URL
