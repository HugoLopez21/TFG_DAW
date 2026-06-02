from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/data/', views.user_data, name='user_data'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/address/add/', views.add_address, name='add_address'),
    path('profile/tracking/', views.tracking_view, name='tracking'),
    path('profile/orders/', views.orders_history, name='orders_history'),
    path('profile/catalog/', views.products_catalog_view, name='products_catalog'),
    path('profile/suggestions/', views.suggestions_view, name='suggestions'),
]