# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juniper', '0015_device_ssh_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='ssh_status',
        ),
    ]