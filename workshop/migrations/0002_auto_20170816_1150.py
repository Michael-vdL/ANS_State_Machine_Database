# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='routine_actions',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='routine_triggers',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='routine_variables',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state_routines',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state_transitions',
        ),
    ]
