from django.contrib import admin
from .models import Producto, Paciente, Consulta

# Register your models here.

admin.site.register(Producto)
admin.site.register(Paciente)
admin.site.register(Consulta)