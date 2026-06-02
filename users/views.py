from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .models import CustomUser
from .forms import ProfileForm, AddressForm
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.



@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('users:user_profile')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
            return render(request, 'users/includes/profile_data.html', {'form': form, 'user': user})
    else:
        form = ProfileForm(instance=user)
        return render(request, 'users/includes/profile_data.html', {'form': form, 'user': user})


@login_required
def add_address(request):
    user = request.user
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            user.addresses.add(address)
            messages.success(request, 'Dirección añadida correctamente.')
            return redirect('users:user_profile')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
            return render(request, 'users/includes/profile_data.html', {'address_form': form, 'user': user})
    return redirect('users:user_profile')




#VISTAS DE RENDERIZACION DE PLANTILLAS
@login_required
def user_profile(request):
    return render(request, 'users/profile.html')


@login_required
def user_data(request):
    if request.method == 'GET':
        user = request.user
        context = {
            'user' : CustomUser.objects.get(id=user.id)
        }
        return render(request, 'users/includes/profile_data.html', context)

@login_required
def tracking_view(request):
    active_order = Order.objects.filter(user=request.user).exclude(status='entregado').first()
    if active_order:
        context = {
            'orderId': active_order.id
        }
    else:
        context = {
            'orderId': None
        }
    return render(request, 'users/includes/tracking.html', context)


@login_required
def products_catalog_view(request):
    return render(request, 'users/includes/products_catalog.html')

@login_required
def orders_history(request):
    return render(request, 'users/includes/orders_history.html')

@login_required
def suggestions_view(request):
    return render(request, 'users/includes/suggestions.html')