# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predds_tracker', '0029_auto_20170130_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='map_auto_update',
            field=models.BooleanField(default=False, help_text='Set map to auto-update or not', verbose_name='Map Autoupdate'),
        ),
    ]