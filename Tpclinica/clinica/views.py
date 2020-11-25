from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Paciente, Consulta, Pedido, PedidoDetalle
from .form import ProductoCreate, PedidoCreate, PedidoDetalleCreate, ConsultaCreate
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django import forms
import datetime

# from .models import Turnos
# from .form import TurnosCreate

# Create your views here.
def index(request):
    #De acuerdo al perfil debemos redeireccionarlo
    return render(request, "index.html")


def productos(request):
    return render(request, "productos.html", {
        "productos": Producto.objects.all()
    })

def producto(request, producto_id):
        unProducto = Producto.objects.get(id=producto_id)
        return render(request, "producto.html",{
            "producto": unProducto
        })

def agregar(request):
    upload  = ProductoCreate()
    if request.method == 'POST':
        upload = ProductoCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('clinica:productos')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'clinica:productos'}}">reload</a>""")
    else:
        return render(request, 'agregar.html', {'upload_form':upload})



def eliminar(request, producto_id):
    producto_id= int(producto_id)
    try:
        producto_sel = Producto.objects.get(id = producto_id)
        
    except Producto.DoesNotExist:
        return redirect('clinica:productos')
    producto_sel.delete()
    return render(request, "eliminar.html")



def actualizar(request, producto_id):
     producto_id = int(producto_id)
     try:
         producto_sel = Producto.objects.get(id = producto_id)
     except Producto.DoesNotExist:
         return redirect('index')
     producto_form = ProductoCreate(request.POST or None, instance = producto_sel)
     if producto_form.is_valid():
        producto_form.save()
        return redirect('clinica:productos')
     return render(request, 'agregar.html', {'upload_form':producto_form })


        
# def crearTurno(request):
#     upload  = TurnosCreate()
#     if request.method == 'POST':
#         upload = TurnosCreate(request.POST, request.FILES)
#         if upload.is_valid():
#             upload.save()
#             return redirect('clinica:turnos')
#         else:
#             return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'clinica:turnos'}}">reload</a>""")
#     else:
#         return render(request, 'agregarturno.html', {'upload_form':upload})



# def borrarTurno(request, turno_id):
#     turno_id = int(turno_id)
#     try:
#         turno_elegido = Turnos.objects.get(id = turno_id)
        
#     except Turnos.DoesNotExist:
#         return redirect('clinica:turnos')
#     turno_elegido.delete()
#     return render(request, "eliminarturno.html")



# def actualizarTurno(request, turno_id):
#      turno_id = int(turno_id)
#      try:
#          turno_elegido = Producto.objects.get(id = turno_id)
#      except Turnos.DoesNotExist:
#          return redirect('index')
#      turno_form = TurnosCreate(request.POST or None, instance = turno_elegido)
#      if turno_form.is_valid():
#         turno_form.save()
#         return redirect('clinica:turnos')
#      return render(request, 'actualizarturno.html', {'upload_form':turno_form })


def pacientes(request):
    return render(request, "pacientes.html", {
        "pacientes": Paciente.objects.all()
    })

def historial(request, paciente_id):
# habria q agregar un if 
    paciente = Paciente.objects.get(id=paciente_id)
    consultasTotales = Consulta.objects.all()
    consultas = consultasTotales.filter(paciente_id=paciente_id)
    return render(request, "historial.html",{
        "consultas": consultas,
        "paciente": paciente,
    })

def agregar_consulta(request):
    upload  = ConsultaCreate()
    if request.method == 'POST':
        upload = ConsultaCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('clinica:pacientes')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'clinica:pacientes'}}">Recargar</a>""")
    else:
        return render(request, 'agregar_consulta.html', {'upload_form':upload})

def eliminar_consulta(request, consulta_id):
    consulta_id= int(consulta_id)
    try:
        consulta_sel = Consulta.objects.get(id = consulta_id)
        
    except Consulta.DoesNotExist:
        return redirect('clinica:pacientes')
    consulta_sel.delete()
    return render(request, "eliminar_consulta.html")

def modificar_consulta(request, consulta_id):
     consulta_id = int(consulta_id)
     try:
         consulta_sel = Consulta.objects.get(id = consulta_id)
     except Consulta.DoesNotExist:
         return redirect('pacientes')
     consulta_form = ConsultaCreate(request.POST or None, instance = consulta_sel)
     if consulta_form.is_valid():
        consulta_form.save()
        return redirect('clinica:pacientes')
     return render(request, 'agregar_consulta.html', {'upload_form':consulta_form })

def pedidos(request):
    return render(request, "pedidos.html", {
        "pedidos": Pedido.objects.all().order_by('-id')
    })

def pedido(request, pedido_id):
        unPedido = Pedido.objects.get(id=pedido_id)
        return render(request, "pedido.html",{
            "pedido": unPedido
        })

def agregar_pedido(request):
    #instanciar la fecha actual
    upload  = PedidoCreate()
    if request.method == 'POST':
        upload = PedidoCreate(request.POST, request.FILES)
        if upload.is_valid():
            f = upload.save(commit=False)
            f.vendedor = request.user
            # f.fecha = datetime.datetime.today
            f.subtotal = float(100)
            f.save()
            pedido = Pedido.objects.last()
            # return redirect('clinica:pedidos')
            # return redirect('clinica:pedido_items', pedido_id=pedido.id)
            # return render(request, 'agregar_item.html', {'upload_form':upload})
            # return HttpResponseRedirect(reverse("clinica:pedido_items", args=(pedido.id)))
            # return reverse_lazy('clinica:pedido_items', kwargs={'pedido_id': pedido.id})

            # return redirect("pedido_items", pedido_id=pedido.id)
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'clinica:pedidos'}}">reload</a>""")
    else:
        return render(request, 'agregar_pedido.html', {'upload_form':upload})



def eliminar_pedido(request, pedido_id):
    pedido_id= int(pedido_id)
    try:
        pedido_sel = Pedido.objects.get(id = pedido_id)
        
    except Pedido.DoesNotExist:
        return redirect('clinica:pedidos')
    pedido_sel.delete()
    return render(request, "eliminar_pedido.html")



def actualizar_pedido(request, pedido_id):
     pedido_id = int(pedido_id)
     try:
         pedido_sel = Pedido.objects.get(id = pedido_id)
     except Pedido.DoesNotExist:
         return redirect('index')
     pedido_form = ProductoCreate(request.POST or None, instance = pedido_sel)
     if pedido_form.is_valid():
        pedido_form.save()
        return redirect('clinica:pedidos')
     return render(request, 'agregar.html', {'upload_form':pedido_form })
        
def pedido_items(request, pedido_id):
     unPedido = Pedido.objects.get(id=pedido_id)
     items = PedidoDetalle.objects.filter(pedido_id=unPedido.id)
     f = formAgregarProducto()
     return render(request, 'pedido_items.html', {'pedido':unPedido, 'items':items, 'form':f})

def agregar_item(request, pedido_id):
    unPedido = Pedido.objects.get(id=pedido_id)
    upload  = PedidoDetalleCreate(instance=unPedido)
    # upload.initial['pedido_id'] = 4
    if request.method == 'POST':
        upload = PedidoDetalleCreate(request.POST, request.FILES)
        if upload.is_valid():
            
            upload.save()
            return redirect('clinica:pedidos')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'clinica:pedidos'}}">reload</a>""")
    else:
        f=formAgregarProducto();
        return render(request, 'agregar_item.html', {'upload_form':upload})

class formAgregarProducto(forms.Form):
    cantidad = forms.IntegerField(label="Cantidad")
    

def detalle_pedido(request, pedido_id):
    unPedido = Pedido.objects.get(id=pedido_id)
    items = PedidoDetalle.objects.filter(pedido_id=unPedido.id)
    #hay que obtener sólo los productos que no están en el pedido
    productos_disponibles = Producto.objects.all()
    return render(request, 'pedido_items.html', {'pedido': unPedido, 'items': items, 'productos_disponibles': productos_disponibles})
     
def agregar_producto(request, pedido_id):
    unPedido = Pedido.objects.get(id=pedido_id)
    detalle_item = PedidoDetalle()
    detalle_item.pedido = unPedido    
    
    if request.method == 'POST':
        detalle_item.producto = Producto.objects.get(id=int(request.POST["productos"]))
        detalle_item.cantidad = int(request.POST["cantidad"])
        detalle_item.save()
        # hay que actualizar el Total del pedido
        items = PedidoDetalle.objects.filter(pedido_id=unPedido.id)
        #hay que obtener sólo los productos que no están en el pedido
        productos_disponibles = Producto.objects.all()
        return render(request, 'pedido_items.html', {'pedido': unPedido, 'items': items, 'productos_disponibles': productos_disponibles})
        # return HttpResponseRedirect(reverse("detalle_pedido", args=(pedido_id)))
    else:
        return render(request, "pedido_items.html", {})