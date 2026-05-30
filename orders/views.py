from django.contrib.auth.decorators import login_required
from .forms import OrderCheckoutForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Order, OrderDetail
from products.models import Product
from django.db import transaction
import json

@login_required
def checkout_form(request):
    user = request.user
    if request.method == 'POST':
        form = OrderCheckoutForm(request.POST)
        # Rellenar con las direcciones del usuario
        form.fields['address'].queryset = user.addresses.all()
        try:
            if form.is_valid():
                #Guardar los datos del formulario
                form_phone_number = form.cleaned_data['phone_number']
                form_delivery_type = form.cleaned_data['delivery_type']
                form_address = form.cleaned_data['address']
                form_notes = form.cleaned_data['notes']
                form_checkout_cart = json.loads(form.cleaned_data['cart_data'])
                
                # Si algo falla se borran los pedidos
                with transaction.atomic():
                    current_order = Order.objects.create(
                        delivery_type = form_delivery_type,
                        total = total_price(form_checkout_cart),
                        pay_status = True,
                        user = user,
                        address = form_address if form_delivery_type == 'home' else None
                    )
                    
                    #Por cada producto del carrito se crea una linea de detalle
                    for item in form_checkout_cart:
                        try:
                            current_product = Product.objects.get(id=item['id'])
                            OrderDetail.objects.create(
                                order = current_order,
                                product = current_product,
                                quantity = item['quantity'],
                                unit_price = current_product.price,
                                notes = form_notes
                            )
                        except Product.DoesNotExist:
                            messages.error(request, 'Error en el pago')
                            return render() # Renderizar checkout
                return redirect() # Redireccion al  template trackin
                
        except Exception as e:
            messages.error(request, 'Error')
            return render() # Form 
        
    elif request.method == 'GET':
        user = request.user
        default_address = user.addresses.first()
        form = OrderCheckoutForm(
            initial={
                'phone_number': user.phone_number,
                'address' : default_address,
            }
        )
        form.fields['address'].queryset = user.addresses.all()
        return render() #Renderiza el template del formulario con la informacion

def total_price(cart):
    try:
        total = 0
        for item in cart:
            product = Product.objects.get(id = item['id'])
            total += product.price * item['quantity']
    except Product.DoesNotExist:
        raise Product.DoesNotExist
    return total