# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eve_sde', '0002_auto_20161220_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='solarsystem',
            name='security',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
