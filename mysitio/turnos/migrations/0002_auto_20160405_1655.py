# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicos',
            name='id',
        ),
        migrations.RemoveField(
            model_name='medicos',
            name='persona',
        ),
        migrations.AddField(
            model_name='medicos',
            name='personas_ptr',
            field=models.OneToOneField(auto_created=True, serialize=False, to='turnos.Personas', default=22, primary_key=True, parent_link=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='especialidades',
            name='mat_especialidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='mat_profesional',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='altura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='perimetro_enc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='peso',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personas',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
