from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.urls import reverse


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name',
                'last_name', 'date_of_birth', 'address', 'city',
                'country', 'post_code')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


