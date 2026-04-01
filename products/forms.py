from django import forms
from .models import Product, Allergen, Category


# Formularios para crear y editar productos, alérgenos y categorías

# PARA DARLE ESTILOS USAREMOS LA LIBRERIA DJANGO-WIDGET-TWEAKS 
# PARA SEPARAR FORNT DE BAKC
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'image', 'prominent', 'on_sale',
            'categories', 'allergens', 'price','is_available'
            ]
        labels = {
            'name' : 'Nombre',
            'description' : 'Descripción',
            'image' : 'Imagen',
            'prominent' : 'Destacado',
            'on_sale' : 'Rebaja',
            'categories' : 'Categorias',
            'allergens' : 'Alérgenos',
            'price' : 'Precio',
            'is_available' : 'Disponible',
        }
        widgets = {
            'description' : forms.Textarea(attrs={'rows' : 3}),
            'allergens' : forms.CheckboxSelectMultiple(),
            'categories' : forms.CheckboxSelectMultiple(),
        }

class AllergenForm(forms.ModelForm):
    class Meta:
        model = Allergen
        fields = ['name', 'icon']
        labels = {
            'name' : 'Nombre',
            'icon' : 'Icono'
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description','image']
        labels = {
            'name' : 'Nombre',
            'description' : 'Descripción',
            'image' : 'Imagen',
        }

        widgets = {
            'description' : forms.Textarea(attrs={'rows' : 3})
        }