from django.contrib import admin
from .models import Product, Allergen, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Personalizaciones del admin irán aquí
    list_display = ('name', 'price')

    # Filtros
    list_filter = ('name',)
    
    # Búsqueda
    search_fields = ('name', 'description')

@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
