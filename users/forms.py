from django.contrib.auth import get_user_model
from django import forms
from django.urls import reverse
from .models import Address
from allauth.account.forms import LoginForm, SignupForm

class CustomSignupForm(SignupForm):
    # Sobre escribe el formulario por defecto de registro de allauth
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(label='Fecha nacimiento (MM-DD-YYYY)')
    phone_number = forms.CharField(max_length=15)

    def save(self, request):
        # Guarda campos adicionales
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    # Formulario para cambio de información manual del usuario
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street', 'number', 'floor_door', 'city', 'post_code')

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)