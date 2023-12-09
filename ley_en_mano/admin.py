from django.contrib import admin
from .models import CustomUser, Caso, Cliente, Abogado

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Caso)
admin.site.register(Cliente)
admin.site.register(Abogado)
