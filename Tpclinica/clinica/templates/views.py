from django.shortcuts import render, redirect
from .models import Producto, Pedido, PedidoDetalle
from .form import ProductoCreate, PedidoCreate, PedidoDetalleCreate
from django.http import HttpResponse
# from .models import Turnos
# from .form import TurnosCreate

# Create your views here.
def index(request):
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

def pedidos(request):
    return render(request, "pedidos.html", {
        "pedidos": Pedido.objects.all()
    })

def pedido(request, pedido_id):
        unPedido = Pedido.objects.get(id=pedido_id)
        return render(request, "pedido.html",{
            "pedido": unPedido
        })

def agregar_pedido(request):
    upload  = PedidoCreate()
    if request.method == 'POST':
        upload = PedidoCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('clinica:pedidos')
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
        return redirect('clinica:productos')
     return render(request, 'agregar.html', {'upload_form':pedido_form })
        
