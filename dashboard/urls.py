from django.urls import path, include
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('pedidos/', views.orders_dashboard, name='orders_dashboard'),
    path('gestion/', views.manager_dashboard, name='manager_dashboard'),
    path('empleados/crear/', views.create_employee, name='create_employee'),
    path('empleados/editar/<int:employee_id>/', views.modify_employee, name='modify_employee'),
    path('empleados/eliminar/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]