from django.contrib.auth.decorators import login_required
from .forms import OrderCheckoutForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderDetail
from products.models import Product
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
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
                form_payment_method = form.cleaned_data['payment_method']
                form_programmed_date = form.cleaned_data['programmed_delivery_date']
                form_checkout_cart = json.loads(form.cleaned_data['cart_data'])
                
                # Tarea 48: Cálculo de tiempo estimado (20 min por pedido activo + el actual)
                pending_orders_count = Order.objects.filter(status__in=['pendiente', 'en_preparacion']).count()
                estimated_minutes = 20 * (pending_orders_count + 1)
                estimated_delivery = timezone.now() + timedelta(minutes=estimated_minutes)

                # Si algo falla se borran los pedidos
                with transaction.atomic():
                    current_order = Order.objects.create(
                        delivery_type = form_delivery_type,
                        total = total_price(form_checkout_cart),
                        pay_status = True if form_payment_method == 'online' else False,
                        user = user,
                        address = form_address if form_delivery_type == 'home' else None,
                        payment_method = form_payment_method,
                        programmed_delivery_date = form_programmed_date,
                        estimated_order_delivery = estimated_delivery
                    )
                    
                    #Por cada producto del carrito se crea una linea de detalle
                    for item in form_checkout_cart:
                        current_product = Product.objects.get(id=item['id'])
                        OrderDetail.objects.create(
                            order = current_order,
                            product = current_product,
                            quantity = item['quantity'],
                            unit_price = current_product.price,
                            notes = form_notes
                        )
                return redirect('orders:order_tracking', order_id=current_order.id)
                
        except Exception as e:
            messages.error(request, 'Hubo un error al procesar tu pedido. Por favor, inténtalo de nuevo.')
            return render(request, 'orders/checkout.html', {'form': form})
        
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
        return render(request, 'orders/checkout.html', {'form': form})

@login_required
def order_tracking(request, order_id):
    # Verificamos que el pedido exista y pertenezca al usuario
    get_object_or_404(Order, id=order_id, user=request.user)
    context = {
            'orderId': order_id
        }
    return render(request, 'users/includes/tracking.html', context)

def total_price(cart):
    try:
        total = 0
        for item in cart:
            product = Product.objects.get(id = item['id'])
            total += product.price * item['quantity']
    except Product.DoesNotExist:
        raise Product.DoesNotExist
    return total