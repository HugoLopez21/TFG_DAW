from django import forms
from .models import Order
from users.models import Address 
import json

# Formulario del checkout que recoge la información del cliente para el pedido
class OrderCheckoutForm(forms.Form):

    phone_number = forms.CharField(
        max_length=15,
        label="Número de teléfono",
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'pattern': '[0-9]+',
        })
    )

    delivery_type = forms.ChoiceField(
        choices=Order.DELIVERY_TYPE,
        label="Elige el tipo de entrega",
        initial='home', # Por defecto
        widget=forms.RadioSelect()
    )

    address = forms.ModelChoiceField(
        queryset=Address.objects.none(), #Conecta con tabla address
        label="Dirección de entrega",
        required=False,  # False porque si eligen 'Pickup' no es necesario
        empty_label="-- Selecciona una dirección guardada --",
        widget=forms.Select()
    )

    notes = forms.CharField(
        max_length=250,
        required=False,
        label="Notas para el pedido",
        widget=forms.Textarea(attrs={
            'placeholder': 'Introduce tus indicaciones personalizadas',
        })
    )

    payment_method = forms.ChoiceField(
        choices=[('online', 'Pagar ahora'), ('in_person', 'Pagar en persona')],
        label="Método de pago",
        initial='online',
        widget=forms.RadioSelect()
    )

    programmed_delivery_date = forms.DateTimeField(
        required=False,
        label="Programar entrega",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    #Validador carrito
    def clean_cart_data(self):
        data = self.cleaned_data.get('cart_data')
        try:
            # Intentamos transformar el texto de React en una lista/objeto Python
            cart_json = json.loads(data)
        except (ValueError, TypeError):
            raise forms.ValidationError("El formato del carrito no es válido.")
            
        # Si el JSON es válido pero está vacio
        if not cart_json:
            raise forms.ValidationError("Tu carrito está vacío. Añade productos antes de pagar.")
            
        return data

    # guardará el JSON del LocalStorage
    cart_data = forms.CharField(
        widget=forms.HiddenInput(),
        required=True
    )
    
    #Validador que evita que si ha elegido a domicilio haya una direccion
    def clean(self):
        cleaned_data = super().clean()
        delivery_type = cleaned_data.get('delivery_type')
        address = cleaned_data.get('address')

        if delivery_type == 'home' and not address:
            raise forms.ValidationError("Si seleccionas envío a domicilio, debes elegir una dirección.")

        return cleaned_data