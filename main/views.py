from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ContactForm
def home(request):
    menu = {
        'products': Product.objects.filter(is_available=True, prominent=True)
    }
    return render(request, 'main/home.html', menu)

@login_required
def login_succes_redirect(request):
    role = request.user.role
    if role == "customer":
        return redirect('main:home')
    elif role == "manager":
        return redirect('dashboard:manager_dashboard')
    elif role in ['delivery_man', 'employee']:
        return redirect('dashboard:orders_dashboard')


def contact_view(request):
    sent = False
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí puedes enviar email con send_mail() o guardar en BD
            sent = True
            form = ContactForm()  # Reset del formulario

    return render(request, 'core/contact.html', {
        'form': form,
        'sent': sent,
    })