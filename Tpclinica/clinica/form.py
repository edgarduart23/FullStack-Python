from django import forms
from .models import  Producto, Consulta, Pedido, PedidoDetalle
# from.models import Turnos
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
        # para la creación no se necesitan
        exclude=('vendedor', 'estado', 'subtotal', 'fecha')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['vendedor'].queryset = User.objects.filter(es_ventas=True)
    
class PedidoUpdate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        # para update solo cambia el estado
        # exclude=('vendedor', 'paciente', 'tipo_pago', 'subtotal', 'fecha')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        

class PedidoDetalleCreate(forms.ModelForm):
    class Meta:
        model = PedidoDetalle
        fields = ('producto', 'cantidad')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
