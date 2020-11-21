from django.db import models

# Create your models here.

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    TIPOS = (('L', 'Lente'), ('E', 'Estuche'), ('G', 'Gotita'))
    tipo = models.CharField(max_length=1, choices=TIPOS)
    ENFOQUE = (('L', 'Lejos'), ('C', 'Cerca'))
    enfoque = models.CharField(max_length=1, choices=ENFOQUE, blank= True)
    LADO = (('I', 'Izqierda'), ('D', 'Derecha'))
    lado = models.CharField(max_length=1, choices=LADO, blank= True)
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
