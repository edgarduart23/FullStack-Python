from django.db import models
from usuarios.models import User
from django.urls import reverse
import datetime
from django.utils import timezone

#  PerfilVentas, PerfilMedico


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


class Paciente(models.Model):
#    medico = models.ForeignKey(PerfilMedico,on_delete=models.SET_NULL,related_name="usuarios_perfilmedico",blank=True,null=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    telefono = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    vendedor = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="user",blank=False,null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="clinica_paciente",blank=False,null=True)
    TIPO_PAGO = (('T', 'Tarjeta de credito'),('B', 'Billetera virtual'),('E', 'Efectivo'),('D', 'Debito'))
    tipo_pago = models.CharField(max_length=1,default='E',choices=TIPO_PAGO)
    ESTADO = (('PT', 'Pendiente'),('PD', 'Pedido'),('TL', 'Taller'),('FP', 'Finalizado'))
    estado = models.CharField( max_length=2,default='PD',choices=ESTADO)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2,default=0.0,blank=True, null=True)
    fecha = models.DateTimeField( default= timezone.now())
    
    def verSubTotal(self):
        return f"$ {self.subtotal}"

class PedidoDetalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.PositiveIntegerField( default=1)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0.0,blank=True)
    """def save(self, *args, **kwargs):
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
            return f"{self.cantidad} {'unidades' if self.cantidad > 1 else 'unidad'}
        def __str__(self):
            return self.producto.nombre"""

class Consulta(models.Model):
#    medico = models.ForeignKey(PerfilVentas,on_delete=models.SET_NULL,related_name="usuarios_medico",blank=True,null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="clinica_paciente.nombre+", blank=False,null=True)
    fecha = models.DateTimeField(null=True, blank=True)
    motivo = models.CharField(max_length=150)
    diagnostico = models.CharField(max_length=150)
    tratamiento = models.CharField(max_length=150)
    observacion = models.CharField(max_length=150)
    def __str__(self):
        return self.motivo

#  viaje de seba con los generic views 
class Turnos(models.Model):
    Paciente = models.ForeignKey(Paciente,  on_delete=models.CASCADE, blank=False,null=True)
#    Medico =models.ForeignKey(User, on_delete=models.SET_NULL,related_name="clinica_medicoid",blank=False,null=True)

    FechaTurno = models.DateField()
    HoraTurno = models.TimeField()
    Opciones = (('P', 'Pendiente'), ('A', 'Asistió'), ('F', 'Faltó'))
    Asistencia = models.CharField(max_length=1, choices=Opciones, blank=True, null=True)
#    FechaAlta = models.DateField(auto_now=True)
#    FechaBaja = models.DateField(blank=True)

    def _str_(self):
        return f"{self.id} {self.Paciente} {self.FechaTurno} {self.HoraTurno} {self.FechaAlta} {self.FechaBaja}"

    def get_absolute_url(self):
        return reverse('clinica:turnos-detail', kwargs={'pk':self.id})

