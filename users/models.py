from django.db import models
from django.contrib.auth.models import AbstractUser

class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    floor_door = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = 'Addresses'

class User(AbstractUser):
    ROLES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('delivery_man', 'Delivery Man'),
        ('manager', 'Manager'),
        ('employee', 'Employee')
    ]
    phone_number = models.CharField(max_length=15)
    
    role = models.CharField(
        max_length=20, 
        choices=ROLES, 
        default='customer'
    )
    
    addresses = models.ManyToManyField(
        Address, 
        blank=True,
        related_name='users'
    )

    def __str__(self):
        return self.name

