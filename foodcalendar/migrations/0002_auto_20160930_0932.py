# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcalendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='ingredient',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
