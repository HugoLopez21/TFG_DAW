from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from users.models import User, Address
from products.models import Product



class OrderState(models.Model):
    name = models.CharField(max_length=50)
    change_data = models.DateTimeField()
    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    estimated_order_delivery = models.DateTimeField()

    DELIVERY_TYPE = [
        ('home', 'Home'),
        ('pickup','Pickup')
    ]
    delivery_type = models.CharField(choices=DELIVERY_TYPE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    programmed_delivery_date = models.DateTimeField()
    pay_state = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    state = models.ForeignKey(OrderState, on_delete=models.PROTECT)

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