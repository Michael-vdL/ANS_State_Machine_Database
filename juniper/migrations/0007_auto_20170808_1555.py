# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juniper', '0006_auto_20170808_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='iface_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]