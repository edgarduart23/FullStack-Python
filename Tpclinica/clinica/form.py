from django import forms
from .models import  Producto
from.models import Turnos

class ProductoCreate(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class TurnosCreate(forms.ModelForm):
    class Meta:
        model = Turnos
        field = '__all__'
