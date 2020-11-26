from django import forms
from .models import  Producto, Consulta, Pedido, PedidoDetalle, Turnos
# from.models import Turnos
from usuarios.models import User

class ProductoCreate(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
#_________________________________________________________________________________________     
class TurnosCreate(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = '__all__'
#________________________________________________________________________

class ConsultaCreate(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class PedidoCreate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        # para la creación no se necesitan
        # exclude=('vendedor', 'estado', 'subtotal', 'fecha')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendedor'].disabled = True
        self.fields['subtotal'].disabled = True
        self.fields['estado'].disabled = True
        self.fields['fecha'].disabled = True
        # self.fields['vendedor'].queryset = User.objects.filter(es_ventas=True)

class PedidoView(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        # para la creación no se necesitan
        # exclude=('vendedor', 'estado', 'subtotal', 'fecha')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendedor'].disabled = True
        self.fields['paciente'].disabled = True
        self.fields['tipo_pago'].disabled = True
        self.fields['estado'].disabled = True
        self.fields['subtotal'].disabled = True
        self.fields['fecha'].disabled = True
    
        

class PedidoDetalleCreate(forms.ModelForm):
    class Meta:
        model = PedidoDetalle
        fields = ('producto', 'cantidad')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
