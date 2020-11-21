from django.db import models

# Create your models here.

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    TIPOS = (('L', 'Lente'), ('E', 'Estuche'), ('G', 'Gotita'))
    tipo = models.CharField(max_length=1, choices=TIPOS)
    def __str__(self):
        return f"{self.id} {self.descripcion} {self.precio} {self.tipo} "

class Turnos(models.Model):
    id = models.IntegerField()
    Paciente = models.ForeignKey(paciente)
    Doctor =models.ForeignKey(doctor)
    FechaTurno = models.DateField()
    HoraTurno = models.DateTimeField()
    FechaAlta = models.DateField()
    FechaBaja = models.DateField()

    def _str_(self):
        return f"{self.id} {self.Paciente} {self.Doctor} {self.FechaTurno} {self.HoraTurno} {self.FechaAlta} {self.FechaBaja}"