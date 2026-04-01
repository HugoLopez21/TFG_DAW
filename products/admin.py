from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Personalizaciones del admin irán aquí
    list_display = ('name', 'price')

    # Filtros
    list_filter = ('name',)
    
    # Búsqueda
    search_fields = ('name', 'description')
