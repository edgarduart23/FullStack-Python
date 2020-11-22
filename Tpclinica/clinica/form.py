from django import forms
from .models import  Producto, Consulta
# from.models import Turnos

class ProductoCreate(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
# class TurnosCreate(forms.ModelForm):
#     class Meta:
#         model = Turnos
#         field = '__all__'

class ConsultaCreate(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'