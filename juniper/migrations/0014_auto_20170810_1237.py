# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 16:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juniper', '0013_ssh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ssh',
            name='device',
        ),
        migrations.DeleteModel(
            name='SSH',
        ),
    ]
