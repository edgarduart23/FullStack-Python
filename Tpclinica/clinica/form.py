from django import forms
from .models import  Producto, Consulta, Pedido, PedidoDetalle
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

class PedidoCreate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        

class PedidoDetalleCreate(forms.ModelForm):
    class Meta:
        model = PedidoDetalle
        fields = '__all__'
        
