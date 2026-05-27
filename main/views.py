from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def login_succes_redirect(request):
    role = request.user.role
    if role == "customer":
        return redirect('home')
    elif role == "manager":
        return redirect() # Vista con decorador de seguridad
    elif role in ['delivery_man', 'employee']:
        return redirect() # Vista con decorador de seguridad