from django.contrib import admin
from .models import CustomUser, Caso, Cliente, Especialidad, Abogado

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Caso)
admin.site.register(Cliente)
admin.site.register(Especialidad)
admin.site.register(Abogado)
