from django.urls import path
from .api import order_list, order_detail



app_name = 'orders'
urlpatterns = [
    path('orders/', order_list, name='orders-list'),  # Endpoint GET, POST
    path('orders/<int:pk>/', order_detail, name='order-detail'),  # Endpoint GET, PUT, DELETE
]