# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constellation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolarSystem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=64, unique=True)),
                ('radius', models.FloatField()),
                ('security', models.FloatField()),
                ('luminosity', models.FloatField()),
                ('border', models.BooleanField()),
                ('corridor', models.BooleanField()),
                ('fringe', models.BooleanField()),
                ('hub', models.BooleanField()),
                ('international', models.BooleanField()),
                ('regional', models.BooleanField()),
                ('constellation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='systems', to='eve_sde.Constellation')),
            ],
        ),
        migrations.AddField(
            model_name='constellation',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='constellations', to='eve_sde.Region'),
        ),
    ]
