from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.urls import reverse


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name',
                'last_name', 'date_of_birth')


# Filtro aplicado al formulario para evitar que se puedan modificar usuarios no empleados
class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_role = self.instance.role
        if user_role != 'delivery_man' and user_role != 'employee':
            raise forms.ValidationError("No se puede modificar este usuario")

    class Meta:
        model = get_user_model()
        fields = '__all__'