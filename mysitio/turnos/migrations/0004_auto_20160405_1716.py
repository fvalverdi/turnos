# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0003_auto_20160405_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='fecha_nac',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
    ]
