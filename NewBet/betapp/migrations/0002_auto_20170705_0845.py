# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='bet',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (0, 0)]),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='fixture_result',
            field=models.IntegerField(blank=True, default=-1),
        ),
    ]
