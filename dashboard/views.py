from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import EmployeeChangeForm, EmployeeCreationForm
from products.models import Product, Category, Allergen
from orders.models import Order



# ------------- COMPROBACIONES DE USUARIOS -------------
def is_manager(user):
    return user.role == "manager"
    
def is_employee(user):
    return user.role in ['delivery_man', 'employee']

def is_worker(user):
    return user.role in ['delivery_man', 'employee', 'manager']


# ------------ RENDERS DE DASHBOARDS -------------------

# RENDERIZA TEMPLATE DE LOS EMPLEADOS
@user_passes_test(is_employee)
def orders_dashboard(request):
    return render(request, 'url') 



# RENDERIZA DASHBOARD DEL MANAGER
@user_passes_test(is_manager)
def manager_dashboard(request):
    User = get_user_model()
    employees = User.objects.filter(role__in=['delivery_man', 'employee'])
    all_products = Product.objects.all()
    available_products = Product.objects.filter(is_available=True)
    no_available_products = Product.objects.filter(is_available=False)
    categories = Category.objects.all()
    allergens = Allergen.objects.all()
    recent_orders = Order.objects.all().order_by('-order_date')[:10]
    context = {
        'employees': employees,
        'all_products': all_products,
        'available_products': available_products,
        'no_available_products': no_available_products,
        'categories': categories,
        'allergens': allergens,
        'recent_orders': recent_orders,
    }
    return render(request, 'dashboard/manager.html', context)



# ----------- VISTAS MANAGER -----------------


# CRUD EMPLEADOS
@user_passes_test(is_manager)
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado creado con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = EmployeeCreationForm()
    return render(request, 'dashboard/employee_form.html', {'form': form, 'title': 'Crear Empleado'})

@user_passes_test(is_manager)
def delete_employee(request, employee_id):
    user = get_object_or_404(get_user_model(), id=employee_id)
    
    if is_manager(user):
        messages.error(request, "No puedes eliminar al manager.")
    else:
        user.delete()
        messages.success(request, "Usuario eliminado con éxito.")
        
    return redirect('dashboard:manager_dashboard')

@user_passes_test(is_manager)
def modify_employee(request, employee_id):
    user = get_object_or_404(get_user_model(), id=employee_id)
    
    if request.method == 'POST':
        form = EmployeeChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado modificado con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = EmployeeChangeForm(instance=user)
        
    return render(request, 'dashboard/employee_form.html', {'form': form, 'title': 'Modificar Empleado', 'employee': user})

# ----------------- VISTAS EMPLEADOS ---------------