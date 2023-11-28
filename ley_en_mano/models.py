from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    APROBADO_CHOICES = (
        ("aprobado", "Aprobado"),
        ("desaprobado", "Desaprobado"),
    )
    aprobado = models.CharField(
        max_length=12, choices=APROBADO_CHOICES, default="desaprobado"
    )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
