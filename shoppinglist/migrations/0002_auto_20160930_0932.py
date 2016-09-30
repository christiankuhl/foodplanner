# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ref_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ref_meal',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
