from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import EmployeeChangeForm, EmployeeCreationForm
from products.models import Product
# Create your views here.



# TODO:
# LIMITAR FUNCIONES SEGUN TIPO DE EMPLEADO
# VISTA (Empleado): REPARTIDOR - COCINA: PARA VER PEDIDOS
# - Modificar pedido

# VISTA (Manager): Gestionar empleados, productos y men



# ------------- COMPROBACIONES DE USUARIOS -------------
def is_manager(user):
    return user.role == "manager"
    
def is_employee(user):
    return user.role in ['delivery_man', 'employee']


# ------------ RENDERS DE DASHBOARDS -------------------

# RENDERIZA TEMPLATE DE LOS EMPLEADOS
@user_passes_test(is_employee)
def orders_dahsboard(request):
    return render(request, 'url') 



# RENDERIZA DASHBOARD DEL MANAGER
@user_passes_test(is_manager)
def manager_dashboard(request):
    User = get_user_model()
    employees = User.objects.filter(role__in=['delivery_man', 'employee'])
    available_products = Product.objects.filter(is_available = True)
    no_available_products = Product.objects.filter(is_available = False)
    context = {
        'employees': employees,
        'available_products' : available_products,
        'no_available_products' : no_available_products,
    }
    return render(request, 'url') # añaldir url y context



# ----------- VISTAS MANAGER -----------------


# CRUD EMPLEADOS
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

# ----------------- VISTAS EMPLEADOS ---------------