from django import forms
from .models import Order


# Formulario de checkout del cliente para tramitar el pedido
class OrderCheckoutForm(forms.ModelForm):
    class Meta:
        pass
