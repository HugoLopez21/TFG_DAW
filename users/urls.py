from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/data/', views.profile_view, name='profile_data'),
    path('profile/tracking/', views.tracking_view, name='tracking'),
    path('profile/orders/', views.orders_history, name='orders_history'),
    path('profile/catalog/', views.products_catalog_view, name='products_catalog'),
    path('profile/suggestions/', views.suggestions_view, name='suggestions'),
]