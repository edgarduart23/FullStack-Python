from django.db import models

# Create your models here.

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    TIPOS = (('L', 'Lente'), ('E', 'Estuche'), ('G', 'Gotita'))
    tipo = models.CharField(max_length=1, choices=TIPOS)
    def __str__(self):
        return f"{self.id} {self.descripcion} {self.precio} {self.tipo} "