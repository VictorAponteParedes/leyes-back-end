from .models import CustomUser, Abogado, Cliente, Caso
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "aprobado", "username", "email", "password"]


class CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caso
        fields = ["id", "nombre", "nro_expediente", "fecha", "materia", "juzgado"]


class ClienteSerializer(serializers.ModelSerializer):
    caso_relacionado = CasoSerializer()

    class Meta:
        model = Cliente
        fields = [
            "id",
            "nombre",
            "edad",
            "telefono",
            "caso_relacionado",
            "is_activo",
            "foto_perfil",
        ]


class AbogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abogado
        fields = [
            "id",
            "nombre",
            "edad",
            "telefono",
            "email",
            "especialidad",
            "foto_perfil",
            "descripcion",
        ]
