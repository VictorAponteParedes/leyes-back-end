from django.shortcuts import render
from .serializers import (
    CustomUserSerializer,
    ClienteSerializer,
    AbogadoSerializer,
    CasoSerializer,
    EspecialidadSerializer,
)
from .models import CustomUser, Cliente, Abogado, Caso, Especialidad

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password


# Create your views here.
@api_view(["POST"])
def registrar_usuario(request):
    if request.method == "POST":
        # Obtener los datos del formulario JSON enviado desde un cliente servidor
        data = request.data
        username = data.get("username")
        password = data.get("password")

        # VALIDA CASO EL USUARIO NO COMPLETE LOS CAMPOS NECESARIOS
        if not username or not password:
            return Response(
                {"error": "Se requieren campos username y password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        hashed_password = make_password(password)
        # Crear un nuevo usuario personalizado
        usuario = CustomUser.objects.create_superuser(
            username=username, password=hashed_password
        )
        usuario.save()
        return Response(
            {"message": "Usuario registrado exitosamente"},
            status=status.HTTP_201_CREATED,
        )


class CustomUserViewset(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class ClienteViewset(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class AbogadoViewset(viewsets.ModelViewSet):
    serializer_class = AbogadoSerializer
    queryset = Abogado.objects.all()


class EspecialidadViewset(viewsets.ModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()


class CasoViewset(viewsets.ModelViewSet):
    serializer_class = CasoSerializer
    queryset = Caso.objects.all()
