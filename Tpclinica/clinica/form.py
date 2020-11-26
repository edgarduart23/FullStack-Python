from django import forms
from .models import  Producto, Consulta, Pedido, PedidoDetalle, Turnos
# from.models import Turnos
from usuarios.models import User
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
import django_filters

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
        widgets = {
            'fecha' : DatePickerInput,
        }

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
        
class Turno_Form(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['Paciente', 'HoraTurno', 'FechaTurno', 'Asistencia']
        widgets = {
            'FechaTurno' : DatePickerInput(),
            'HoraTurno' : TimePickerInput(),
        }

