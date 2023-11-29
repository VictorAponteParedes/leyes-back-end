from .models import CustomUser, Especialidad, Abogado, Cliente, Caso
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


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ["id", "nombre"]


class AbogadoSerializer(serializers.ModelSerializer):
    cliente_relacionado = ClienteSerializer()
    especialidad = EspecialidadSerializer()

    class Meta:
        model = Abogado
        fields = [
            "id",
            "nombre",
            "edad",
            "telefono",
            "cliente_relacionado",
            "foto_perfil",
            "especialidad",
            "descripcion",
        ]
