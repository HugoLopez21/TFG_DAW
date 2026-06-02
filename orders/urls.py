from django.urls import path
from .api import order_list, order_detail
from . import views



app_name = 'orders'
urlpatterns = [

    # Vistas
    path('checkout/', views.checkout_form, name='checkout'),
    path('tracking/<int:order_id>/', views.order_tracking, name='order_tracking'),
    
    # Api endpoints
    path('', order_list, name='orders-list'),  # Endpoint GET
    path('<int:pk>/', order_detail, name='order-detail'),  # Endpoint GET, PUT
]