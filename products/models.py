from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='undefinied',
        null=True,
        blank=True
    )
    date_of_creation = models.DateTimeField(auto_now_add=True)


class Allergen(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(
        upload_to='undefinied',
        null=True,
        blank=True
    )

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='undefinied',
        null=True,
        blank=True
    )
    prominent = models.BooleanField(default = False)
    date_of_creation = models.DateTimeField(auto_now_add = True)
    date_of_update = models.DateTimeField(auto_now = True)
    on_sale = models.BooleanField(default=False)
    category = models.ManyToManyField(
        Category, 
        related_name='products'
        )
    allergens = models.ManyToManyField(
        Allergen,
        related_name='products'
        )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
