from django import forms
from .models import  Producto, Consulta
# from.models import Turnos
from .models import  Pedido
from .models import  PedidoDetalle
from usuarios.models import User

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
        #exclude=('vendedor',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendedor'].queryset = User.objects.filter(es_ventas=True)
    
        

class PedidoDetalleCreate(forms.ModelForm):
    class Meta:
        model = PedidoDetalle
        fields = '__all__'
        
