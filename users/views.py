from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order

# Create your views here.
@login_required
def user_profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_view(request):
    return render(request, 'users/includes/profile_data.html')

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