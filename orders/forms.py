from django import forms
from .models import Order


# Formulario de checkout del cliente para tramitar el pedido
class OrderCheckoutForm(forms.ModelForm):
    class Meta:
        pass

# Formulario para actualizar el estado del pedido por parte del personal
class OrderStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            # Este widget permite elegir una de las opciones de estado
            'status': forms.RadioSelect(),
        } 