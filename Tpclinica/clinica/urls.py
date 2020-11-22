from django.urls import path, include
from . import views

app_name= "clinica"
urlpatterns = [
    path('',  views.index, name="index"),
    path('productos',  views.productos, name="productos"),
    path('productos/<int:producto_id>',  views.producto, name="producto"),
    path('productos/agregar',  views.agregar, name="agregar"),
    path('productos/eliminar/<int:producto_id>',  views.eliminar, name="eliminar"),
    path('productos/actualizar/<int:producto_id>',  views.actualizar, name="actualizar"),
    # path('turnos/crear', views.crearTurno , name = "crearTurno"),
    # path('turnos/actualizar/<int:turno_id>', views.actualizarTurno, name = "actualizarTurno"),
    # path('turnos/eliminar/<int:turno_id', views.borrarTurno, name ="borrarTurno"),
    path('pedidos',  views.pedidos, name="pedidos"),
    path('pedidos/<int:pedido_id>',  views.pedido, name="pedido"),
    path('pedidos/agregar',  views.agregar_pedido, name="agregar_pedido"),
    path('pedidos/eliminar/<int:pedido_id>',  views.eliminar_pedido, name="eliminar_pedido"),
    path('pedidos/actualizar/<int:pedido_id>',  views.actualizar_pedido, name="actualizar_pedido"),
    
]
