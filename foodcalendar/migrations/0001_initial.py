# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.CharField(max_length=255)),
                ('member', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('meal', models.CharField(max_length=255)),
                ('whoiscooking', models.CharField(max_length=255)),
                ('ingredient', models.CharField(max_length=255)),
                ('created', models.DateTimeField(verbose_name=b'auto_now_add=True')),
                ('ingredient_there', models.BooleanField()),
            ],
        ),
    ]
