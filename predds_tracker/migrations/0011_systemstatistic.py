# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eve_sde', '0003_solarsystem_security'),
        ('predds_tracker', '0010_systemmetadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(db_index=True)),
                ('ship_kills', models.IntegerField()),
                ('pod_kills', models.IntegerField()),
                ('npc_kills', models.IntegerField()),
                ('system', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='eve_sde.SolarSystem')),
            ],
        ),
    ]
