
'''
Este archivo define los modelos para el Pedido y el Detalle del Pedido,
que representan los pedidos realizados por los usuarios y los detalles 
de cada pedido, respectivamente.
'''
from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator

#Importar modelos requeridos del proyecto
from users.models import CustomUser, Address
from products.models import Product




class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)

    # Puede ser null porque el pedido puede no tener una fecha 
    # de entrega estimada al momento de su creación.
    estimated_order_delivery = models.DateTimeField(null=True, blank=True)

    # Elección para el tipo de entrega.
    DELIVERY_TYPE = [
        ('home', 'Home'),
        ('pickup','Pickup')
    ]
    delivery_type = models.CharField(max_length=30, choices=DELIVERY_TYPE)
    
    
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    programmed_delivery_date = models.DateTimeField(null=True, blank=True)
    pay_status = models.BooleanField(default =False)

    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Puede ser null porque el pedido puede ser para recoger
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)

    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_preparacion', 'En preparación'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    status = models.CharField(max_length=30, choices = STATUS_CHOICES, default='pendiente')
    status_change_data = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, 
        related_name='details', 
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=250, blank=True)


    @property
    def subtotal(self):
        ''' 
        Método de clase que calcula el coste del pedido completo (subtotal)
        
        Se pone el decorador property para poder acceder 
        desde los templates.
        '''
        return self.unit_price * self.quantity