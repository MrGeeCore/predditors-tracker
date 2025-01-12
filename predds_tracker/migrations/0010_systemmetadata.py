# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eve_sde', '0003_solarsystem_security'),
        ('predds_tracker', '0009_character_track'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('important', models.BooleanField()),
                ('note', models.TextField()),
                ('system', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='eve_sde.SolarSystem')),
            ],
        ),
    ]
