from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_view(request):
    return render(request, 'users/includes/profile_data.html')

@login_required
def tracking_view(request):
    return render(request, 'users/includes/tracking.html')

@login_required
def products_catalog_view(request):
    return render(request, 'users/includes/products_catalog.html')

@login_required
def orders_history(request):
    return render(request, 'users/includes/orders_history.html')

@login_required
def suggestions_view(request):
    return render(request, 'users/includes/suggestions.html')