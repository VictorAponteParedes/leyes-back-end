import os
import uuid


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
def imagen_cliente(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (str(uuid.uuid4()).replace("-", ""), ext)
    return os.path.join("cliente", filename)


def imagen_abogado(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (str(uuid.uuid4()).replace("-", ""), ext)
    return os.path.join("abogado", filename)


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


class Caso(models.Model):
    MATERIA_CHOICES = (
        ("laboral", "Laboral"),
        ("civil y comercial", "Civil y Comercial"),
        ("administrativo", "Administrativo"),
        ("penal", "Penal"),
        ("niñez y adolecencia", "Niñez y Adolecencia"),
    )
    nombre = models.CharField(max_length=40, null=True)
    nro_expediente = models.IntegerField(default=0, null=True)
    fecha = models.DateField()
    materia = models.CharField(
        max_length=20, choices=MATERIA_CHOICES, default="laboral"
    )
    juzgado = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(
        "Edad", blank=False, help_text="Ingrese su edad", default=18
    )
    telefono = models.IntegerField("Celular", default=None)
    caso_relacionado = models.ForeignKey(Caso, on_delete=models.CASCADE)
    is_activo = models.BooleanField(default=False)
    foto_perfil = models.ImageField(upload_to=imagen_cliente, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Abogado(models.Model):
    nombre = models.CharField("Nombre", max_length=50, null=True)
    edad = models.IntegerField("Edad", null=True, blank=True, default=20)
    telefono = models.IntegerField("Celular", default=None)
    cliente_relacionado = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to=imagen_abogado, null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    descripcion = models.TextField(
        null=True,
        blank=True,
        default="descripcion",
    )

    def __str__(self):
        return self.nombre
