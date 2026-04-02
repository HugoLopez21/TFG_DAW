from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse

class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    floor_door = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = 'Addresses'
        #Evitar dos direcciones iguales en la bd
        unique_together = ('street', 'number', 'floor_door', 'city', 'post_code')

    def __str__(self):
        return f"{self.street} {self.number}, {self.city}"


class CustomUserManager(BaseUserManager):
    # Usa mail en lugar del username

    def create_user(self, email, password, **extra_fields):
        # Crea al usuario con el mail y la contraseña pasada por parametro
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Crea al Super usuario con el mail y la contraseña pasada por parametro
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Validaciones 
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    # Ampliar los campos del modelo de usuarios de django 

    username = None
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(max_length=15)
    
    # Lista de roles de los usuarios
    ROLES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('delivery_man', 'Delivery Man'),
        ('manager', 'Manager'),
        ('employee', 'Employee')
    ]
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

    date_of_birth = models.DateField(null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 
        'last_name', 
        'date_of_birth'
    ]

    # Reasigna objects para usar la logica personalizada 
    # de creación de users
    objects = CustomUserManager() 
    def __str__(self):
        return self.first_name

    #Obtener url perfil del usuario
    def get_absolute_url(self):
        return reverse('user_profile')