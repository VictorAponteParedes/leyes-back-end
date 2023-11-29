from rest_framework import routers
from django.urls import include, path
from .views import (
    CustomUserViewset,
    ClienteViewset,
    AbogadoViewset,
    EspecialidadViewset,
    CasoViewset,
)


routers = routers.DefaultRouter()

routers.register(r"usuarios", CustomUserViewset, "usuarios")
routers.register(r"cliente", ClienteViewset, "cliente")
routers.register(r"abogado", AbogadoViewset, "abogado")
routers.register(r"especialidad", EspecialidadViewset, "especialidad")
routers.register(r"caso", CasoViewset, "caso")


urlpatterns = [path("", include(routers.urls))]
