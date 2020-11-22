from django.db import models
from usuarios.models import PerfilVentas


# Create your models here.

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    TIPOS = (('L', 'Lente'), ('E', 'Estuche'), ('G', 'Gotita'))
    tipo = models.CharField(max_length=1, choices=TIPOS)
    ENFOQUE = (('L', 'Lejos'), ('C', 'Cerca'))
    enfoque = models.CharField(max_length=1, choices=ENFOQUE, blank= True, null=True)
    LADO = (('I', 'Izqierda'), ('D', 'Derecha'))
    lado = models.CharField(max_length=1, choices=LADO, blank= True, null=True)
    armazon = models.BooleanField(default=False)
   
    def __str__(self):
        return f"{self.id} {self.descripcion} {self.precio} {self.tipo} "

# class Paciente(models.Model):
#     nombre = models.CharField(max_length = 120)
    # place = models.OneToOneField(
    #     Place,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
# class Doctor(models.Model):
#     nombre = models.CharField(max_length = 120)
    # place = models.OneToOneField(
    #     Place,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    #     nombre = models.CharField(max_length = 120)
    # )

# class Turnos(models.Model):
#     id = models.IntegerField()
#     Paciente = models.ForeignKey(Paciente,  on_delete=models.CASCADE)
#     Doctor =models.ForeignKey(Doctor,  on_delete=models.CASCADE)
#     FechaTurno = models.DateField()
#     HoraTurno = models.DateTimeField()
#     FechaAlta = models.DateField()
#     FechaBaja = models.DateField()

#     def _str_(self):
#         return f"{self.id} {self.Paciente} {self.Doctor} {self.FechaTurno} {self.HoraTurno} {self.FechaAlta} {self.FechaBaja}"


class Pedido(models.Model):
    vendedor = models.ForeignKey(PerfilVentas,on_delete=models.SET_NULL,related_name="usuarios_perfiltaller",blank=True,null=True)
    #paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    TIPO_PAGO = (('T', 'Tarjeta de credito'),('B', 'Billetera virtual'),('E', 'Efectivo'),('D', 'Debito'))
    tipo_pago = models.CharField(max_length=1,default='E',choices=TIPO_PAGO)
    ESTADO = (('PT', 'Pendiente'),('PD', 'Pedido'),('TL', 'Taller'),('FP', 'Finalizado'))
    estado = models.CharField( max_length=2,default='PD',choices=ESTADO)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2,default=0.0,blank=True, null=True)
    fecha = models.DateField( default= None)
    def __str__(self):
        return f"{self.paciente.nombre} {self.paciente.apellido}"
    def verSubTotal(self):
        return f"$ {self.subtotal}"

class PedidoDetalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.PositiveIntegerField( default=1)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.0,blank=True)
    def save(self, *args, **kwargs):
        self.total = self.producto.precio * Decimal(self.cantidad)  
        producto = Producto.objects.get(id=self.producto.id)
        pedido = Pedido.objects.get(id=self.pedido.id)
        detalle = DetallePedido.objects.filter(id=self.id)
        if detalle:
            if self.cantidad > detalle[0].cantidad:
                pedido.subtotal += self.total - detalle[0].total
            else:
                pedido.subtotal -= detalle[0].total - self.total
        else:
            if pedido.subtotal:
                pedido.subtotal += self.total
            else:
                pedido.subtotal = self.total
        producto.save()
        pedido.save()
        super().save(*args, **kwargs)
        def obtenerCantidad(self):
            return f"{self.cantidad} {'unidades' if self.cantidad > 1 else 'unidad'}"
        def __str__(self):
            return self.producto.nombre
