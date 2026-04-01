from django import forms
from .models import Product, Allergen, Category


# Formularios para crear y editar productos, alérgenos y categorías

class ProductForm(forms.ModelForm):
    class Meta:
        pass

class AllergenForm(forms.ModelForm):
    class Meta:
        pass

class CategoryForm(forms.ModelForm):
    class Meta:
        pass