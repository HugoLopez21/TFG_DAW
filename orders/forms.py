from django import forms
from .models import Order


# Formulario de checkout del cliente para tramitar el pedido
class OrderCheckoutForm(forms.ModelForm):
    class Meta:
        pass

# Formulario para actualizar el estado del pedido por parte del personal
class OrderStatusUpdateForm(forms.ModelForm):
    class Meta:
        pass