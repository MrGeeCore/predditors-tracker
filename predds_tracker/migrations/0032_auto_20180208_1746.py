# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-08 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predds_tracker', '0031_auto_20170507_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alt',
            name='alliance_id',
        ),
        migrations.RemoveField(
            model_name='alt',
            name='corporation_id',
        ),
        migrations.RemoveField(
            model_name='character',
            name='alliance_id',
        ),
        migrations.RemoveField(
            model_name='character',
            name='corporation_id',
        ),
    ]
