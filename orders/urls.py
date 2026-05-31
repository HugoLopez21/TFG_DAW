from django.urls import path
from .api import order_list, order_detail
from . import views



app_name = 'orders'
urlpatterns = [

    # Vistas
    path('checkout/', views.checkout_form, name='checkout'),
    path('tracking/<int:order_id>/', views.order_tracking, name='order_tracking'),
    
    # Api endpoints
    path('orders/', order_list, name='orders-list'),  # Endpoint GET
    path('orders/<int:pk>/', order_detail, name='order-detail'),  # Endpoint GET, PUT
]