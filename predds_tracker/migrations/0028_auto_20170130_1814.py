# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predds_tracker', '0027_remove_character_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='alt',
            name='alliance_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='alt',
            name='corporation_id',
            field=models.BigIntegerField(null=True),
        ),
    ]