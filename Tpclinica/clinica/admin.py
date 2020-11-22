from django.contrib import admin
from .models import Producto, Paciente, Consulta, Pedido, PedidoDetalle

# Register your models here.

admin.site.register(Producto)
admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)