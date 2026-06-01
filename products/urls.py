from django.urls import path
from .api import products_list
from . import views

app_name = 'products'
urlpatterns = [
    # CRUD Productos
    path('crear/', views.create_product, name='create_product'),
    path('editar/<int:product_id>/', views.modify_product, name='modify_product'),
    path('eliminar/<int:product_id>/', views.delete_product, name='delete_product'),
    path('alternar-disponibilidad/<int:product_id>/', views.toggle_product_availability, name='toggle_availability'),
    
    # CRUD Categorías
    path('categoria/crear/', views.create_category, name='create_category'),
    path('categoria/editar/<int:category_id>/', views.modify_category, name='modify_category'),
    path('categoria/eliminar/<int:category_id>/', views.delete_category, name='delete_category'),
    
    # CRUD Alérgenos
    path('alergeno/crear/', views.create_allergen, name='create_allergen'),
    path('alergeno/editar/<int:allergen_id>/', views.modify_allergen, name='modify_allergen'),
    path('alergeno/eliminar/<int:allergen_id>/', views.delete_allergen, name='delete_allergen'),

    # API ENDPOINT
    path('/products/', products_list, name='products_list')
]