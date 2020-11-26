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
        
# class TurnosCreate(forms.ModelForm):
#     class Meta:
#         model = Turnos
#         field = '__all__'

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
        #exclude=('vendedor',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendedor'].queryset = User.objects.filter(es_ventas=True)
           

class PedidoDetalleCreate(forms.ModelForm):
    class Meta:
        model = PedidoDetalle
        fields = '__all__'
        
class Turno_Form(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['Paciente', 'HoraTurno', 'FechaTurno', 'Asistencia']
        widgets = {
            'FechaTurno' : DatePickerInput(),
            'HoraTurno' : TimePickerInput(),
        }

