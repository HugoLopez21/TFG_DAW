from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.urls import reverse



class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'first_name', 'last_name', 'role')


# Filtro aplicado al formulario para evitar que se puedan modificar usuarios no empleados
class EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # Clean para revisar si los datos son validos
    def clean(self):   
        cleaned_data = super().clean()
        user_role = self.instance.role
        if user_role != 'delivery_man' and user_role != 'employee':
            raise forms.ValidationError("No se puede modificar este usuario")
        return cleaned_data
    