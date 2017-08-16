# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('routine_name', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('routine_description', models.CharField(max_length=1000)),
                ('routine_type', models.CharField(max_length=6)),
                ('routine_triggers', jsonfield.fields.JSONField()),
                ('routine_variables', jsonfield.fields.JSONField()),
                ('routine_actions', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_name', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('state_type', models.CharField(max_length=6)),
                ('state_routines', jsonfield.fields.JSONField()),
                ('state_transitions', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('transition_name', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('transition_destination', models.CharField(max_length=25)),
                ('transition_security', models.BooleanField(default=False)),
            ],
        ),
    ]