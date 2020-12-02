from .models import Turnos, Paciente
import django_filters
from django_filters import DateFilter, CharFilter
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class TurnosFilter(django_filters.FilterSet):

    Anio = django_filters.NumberFilter(field_name="FechaTurno", lookup_expr='year')
    Mes = django_filters.NumberFilter(field_name="FechaTurno", lookup_expr='month')
    Dia = django_filters.NumberFilter(field_name="FechaTurno", lookup_expr='day')


    class Meta:
        model = Turnos
        fields = ['Paciente', 'Anio', 'Mes', 'Dia']
        widgets = {
            'Anio' : DatePickerInput(),
            'Mes' : DatePickerInput(),
            'Dia' : DatePickerInput(),

        }


class ReporteFilter(django_filters.FilterSet):

    Anio = django_filters.NumberFilter(field_name="FechaTurno", lookup_expr='year')
    Mes = django_filters.NumberFilter(field_name="FechaTurno", lookup_expr='month')
    Dia = django_filters.NumberFilter(field_name="FechaTurno", lookup_expr='day')


    class Meta:
        model = Turnos
        fields = ['Paciente', 'Asistencia', 'Anio', 'Mes', 'Dia']
        widgets = {
            'Anio' : DatePickerInput(),
            'Mes' : DatePickerInput(),
            'Dia' : DatePickerInput(),

        }


# class ObservacionFilter(django_filters.FilterSet):
#     fecha = DateFilter(field_name="Fecha", lookup_expr='gte')

#     class Meta:
#         model = Observacion
#         fields = ['Paciente', 'Fecha']
#         widgets = {
#             'fecha' : DatePickerInput(),

#         }