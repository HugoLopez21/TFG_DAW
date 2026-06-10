# core/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        max_length=150,
        widget=forms.TextInput(attrs={
            'id': 'name',
            'class': 'form-input',
            'required': True,
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'class': 'form-input',
            'required': True,
        })
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={
            'id': 'message',
            'class': 'form-input',
            'rows': 4,
            'required': True,
        })
    )