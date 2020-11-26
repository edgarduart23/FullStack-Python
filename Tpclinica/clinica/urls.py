from django.urls import path, include
from .views import TurnoCreate, TurnoDelete, TurnoUpdate
from . import views

app_name= "clinica"
urlpatterns = [
    path('',  views.index, name="index"),
    path('productos',  views.productos, name="productos"),
    path('productos/<int:producto_id>',  views.producto, name="producto"),
    path('productos/agregar',  views.agregar, name="agregar"),
    path('productos/eliminar/<int:producto_id>',  views.eliminar, name="eliminar"),
    path('productos/actualizar/<int:producto_id>',  views.actualizar, name="actualizar"),
    path('pacientes',  views.pacientes, name="pacientes"),
    path('historial/<int:paciente_id>',  views.historial, name="historial"),
    path('historial/agregar_consulta',  views.agregar_consulta, name="agregar_consulta"),
    path('historial/eliminar_consulta/<int:consulta_id>',  views.eliminar_consulta, name="eliminar_consulta"),
    path('historial/modificar_consulta/<int:consulta_id>',  views.modificar_consulta, name="modificar_consulta"),

    # path('turnos/crear', views.crearTurno , name = "crearTurno"),
    # path('turnos/actualizar/<int:turno_id>', views.actualizarTurno, name = "actualizarTurno"),
    # path('turnos/eliminar/<int:turno_id', views.borrarTurno, name ="borrarTurno"),
    path('pedidos',  views.pedidos, name="pedidos"),
    path('pedidos/<int:pedido_id>',  views.pedido, name="pedido"),
    path('pedidos/agregar',  views.agregar_pedido, name="agregar_pedido"),
    path('pedidos/eliminar/<int:pedido_id>',  views.eliminar_pedido, name="eliminar_pedido"),
    path('pedidos/actualizar/<int:pedido_id>',  views.actualizar_pedido, name="actualizar_pedido"),
    path('pedidos/pedido_items/<int:pedido_id>/',  views.pedido_items, name="pedido_items"),
    path('pedidos/pedido_items/<int:pedido_id>/agregar_item',  views.agregar_item, name="agregar_item"),
#  viaje de seba con los generic views 
    path('turnos/', views.TurnosListView.as_view(), name='turnos'),
    path('turnos/<int:pk>', views.TurnoDetailView.as_view(), name='turnos-detail'),
    path('turnos/create/', TurnoCreate.as_view(), name='turno-create'),
    path('turnos/<int:pk>/update/', TurnoUpdate.as_view(), name='turno-update'),
    path('turnos/<int:pk>/delete/', TurnoDelete.as_view(), name='turno-delete'),
    path('turnos/reporte',  views.turnos_reporte, name="turnos_reporte"),


]
