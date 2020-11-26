from .models import Turnos, Paciente
import django_filters
from django_filters import DateFilter, CharFilter
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class TurnosFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="FechaTurno", lookup_expr='gte')
    end_date = DateFilter(field_name="FechaTurno", lookup_expr='lte')

    class Meta:
        model = Turnos
        fields = ['Paciente', 'Asistencia']
        widgets = {
            'start_date' : DatePickerInput(),
            'end_date' : DatePickerInput(),

        }