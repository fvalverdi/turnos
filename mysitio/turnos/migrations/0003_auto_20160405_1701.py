# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_auto_20160405_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacientes',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='persona',
        ),
        migrations.AddField(
            model_name='pacientes',
            name='personas_ptr',
            field=models.OneToOneField(to='turnos.Personas', primary_key=True, serialize=False, default=22, parent_link=True, auto_created=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='fecha_inicio',
            field=models.DateField(verbose_name='Fecha de Alta Como paciente'),
        ),
    ]
