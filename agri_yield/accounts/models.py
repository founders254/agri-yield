from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_permissions_set',
        blank=True
    )

    def __str__(self):
        return self.username

