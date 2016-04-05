# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('mat_especialidad', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Historias_medicas',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha_historia', models.DateTimeField(verbose_name='Fecha de Creacion')),
                ('diagnostico', models.CharField(max_length=500)),
                ('tratamiento', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('mat_profesional', models.IntegerField(max_length=6)),
                ('especialidad', models.ForeignKey(to='turnos.Especialidades')),
            ],
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('domicilio', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha de Alta Como paciente')),
                ('altura', models.IntegerField(max_length=4)),
                ('peso', models.IntegerField(max_length=5)),
                ('perimetro_enc', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=100)),
                ('fecha_nac', models.DateTimeField(verbose_name='Fecha de nacimiento')),
                ('domicilio', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('dni', models.IntegerField(max_length=10)),
                ('sexo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateTimeField(verbose_name='Fecha del Turno')),
                ('medico', models.ForeignKey(to='turnos.Medicos')),
                ('organizacion', models.ForeignKey(to='turnos.Organizacion')),
                ('paciente', models.ForeignKey(to='turnos.Pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('organizacion', models.ForeignKey(to='turnos.Organizacion')),
                ('persona', models.ForeignKey(to='turnos.Personas')),
                ('tipo_usuario', models.ForeignKey(to='turnos.Tipo_Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='turnos',
            name='usuario',
            field=models.ForeignKey(to='turnos.Usuarios'),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='persona',
            field=models.ForeignKey(to='turnos.Personas'),
        ),
        migrations.AddField(
            model_name='medicos',
            name='persona',
            field=models.ForeignKey(to='turnos.Personas'),
        ),
        migrations.AddField(
            model_name='historias_medicas',
            name='medico',
            field=models.ForeignKey(to='turnos.Medicos'),
        ),
        migrations.AddField(
            model_name='historias_medicas',
            name='paciente',
            field=models.ForeignKey(to='turnos.Pacientes'),
        ),
    ]
