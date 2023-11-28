from rest_framework import routers
from django.urls import include, path
from .views import CustomUserViewset


routers = routers.DefaultRouter()

routers.register(r"usuarios", CustomUserViewset, "usuarios")


urlpatterns = [path("", include(routers.urls))]
