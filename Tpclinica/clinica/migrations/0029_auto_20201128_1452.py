# Generated by Django 3.1.3 on 2020-11-28 17:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinica', '0028_auto_20201128_0636'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='turnos',
        #     name='FechaAlta',
        # ),
        # migrations.RemoveField(
        #     model_name='turnos',
        #     name='FechaBaja',
        # ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor-consulta+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paciente',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor-paciente+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 17, 52, 19, 283131, tzinfo=utc)),
        ),
    ]
