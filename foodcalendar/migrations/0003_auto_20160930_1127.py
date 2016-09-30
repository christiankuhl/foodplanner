# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcalendar', '0002_auto_20160930_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='whoiscooking',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
