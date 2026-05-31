from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Product, Allergen, Category
from .forms import ProductForm, AllergenForm, CategoryForm
from dashboard.views import is_manager 
from django.db.models import ProtectedError

#-------------- CRUD DE PRODUCTOS ------------


@user_passes_test(is_manager)
def create_product(request):
    if request.method == 'POST':
        # request.FILES para imágenes
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Crear Producto'})

@user_passes_test(is_manager)
def modify_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto modificado con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = ProductForm(instance = product)
    return render(request, 'products/product_form.html', {'form': form, 'product': product, 'title': 'Editar Producto'})


@user_passes_test(is_manager)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, f"El producto '{product.name}' ha sido eliminado.")
    return redirect('dashboard:manager_dashboard')



#-------------- CRUD DE CATEGORÍAS -----------------


@user_passes_test(is_manager)
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form, 'title': 'Crear Categoría'})


@user_passes_test(is_manager)
def modify_category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría modificada con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = CategoryForm(instance = category)
    return render(request, 'products/category_form.html', {'form': form, 'category': category, 'title': 'Editar Categoría'})


@user_passes_test(is_manager)
def delete_category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    try:
        category.delete()
        messages.success(request, f"La categoría '{category.name}' ha sido eliminada.")
    except ProtectedError:
        messages.error(request, 'No puedes borrar esta categoría porque contiene productos asociados')
    return redirect('dashboard:manager_dashboard')



#--------- CRUD DE ALÉRGENOS ---------------


@user_passes_test(is_manager)
def create_allergen(request):
    if request.method == 'POST':
        form = AllergenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Alérgeno creado con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = AllergenForm()
    return render(request, 'products/allergen_form.html', {'form': form, 'title': 'Crear Alérgeno'})


@user_passes_test(is_manager)
def modify_allergen(request, allergen_id):
    allergen = get_object_or_404(Allergen, id= allergen_id)
    if request.method == 'POST':
        form = AllergenForm(request.POST, request.FILES, instance=allergen)
        if form.is_valid():
            form.save()
            messages.success(request, "Alérgeno modificado con éxito.")
            return redirect('dashboard:manager_dashboard')
    else:
        form = AllergenForm(instance=allergen)
    return render(request, 'products/allergen_form.html', {'form': form, 'allergen': allergen, 'title': 'Editar Alérgeno'})


@user_passes_test(is_manager)
def delete_allergen(request, allergen_id):
    allergen = get_object_or_404(Allergen, id= allergen_id)
    allergen.delete()
    messages.success(request, f"El alérgeno '{allergen.name}' ha sido eliminado.")
    return redirect('dashboard:manager_dashboard')


#--------- TOGGLE DISPONIBILIDAD DEL PRODUCTO ---------------

@user_passes_test(is_manager)
def toggle_product_availability(request, product_id):
    """Alterna el estado de disponibilidad (activo/inactivo) de un producto"""
    product = get_object_or_404(Product, id=product_id)
    product.is_available = not product.is_available
    product.save()
    
    estado = "activado" if product.is_available else "desactivado"
    messages.success(request, f"Producto '{product.name}' ha sido {estado}.")
    return redirect('dashboard:manager_dashboard')