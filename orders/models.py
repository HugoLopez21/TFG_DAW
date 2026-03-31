from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from users.models import User, Address
from products.models import Product



class OrderState(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    estimated_order_delivery = models.DateTimeField(null=True, blank=True)

    DELIVERY_TYPE = [
        ('home', 'Home'),
        ('pickup','Pickup')
    ]
    delivery_type = models.CharField(choices=DELIVERY_TYPE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    programmed_delivery_date = models.DateTimeField(null=True, blank=True)
    pay_state = models.BooleanField(default =False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(OrderState, on_delete=models.PROTECT)
    state_change_data = models.DateTimeField(auto_now_add=True, null=True, blank=True)

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
        return self.unit_price * self.quantity