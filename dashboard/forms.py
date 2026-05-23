from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.urls import reverse


# TODO:
# Hacer que solo sean modificables los usuarios con rol empleados

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name',
                'last_name', 'date_of_birth')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


# TODO:
#   - Formulario de gestion del menú



