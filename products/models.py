from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='undefinied',
        null=True,
        blank=True
    )
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Categories'



class Allergen(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(
        upload_to='undefinied',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name

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
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
