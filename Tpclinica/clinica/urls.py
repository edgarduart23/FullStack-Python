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
    path('pacientes',  views.pacientes, name="pacientes"),
    path('historial/<int:paciente_id>',  views.historial, name="historial"),

    # path('turnos/crear', views.crearTurno , name = "crearTurno"),
    # path('turnos/actualizar/<int:turno_id>', views.actualizarTurno, name = "actualizarTurno"),
    # path('turnos/eliminar/<int:turno_id', views.borrarTurno, name ="borrarTurno"),
]
