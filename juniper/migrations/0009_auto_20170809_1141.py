# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juniper', '0008_auto_20170808_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=15)),
                ('remote', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Address_Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Logical_Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logface_name', models.CharField(max_length=50)),
                ('log_admin_status', models.CharField(max_length=4)),
                ('log_oper_status', models.CharField(max_length=4)),
                ('physical_interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juniper.Interface')),
            ],
        ),
        migrations.AddField(
            model_name='address_family',
            name='logical_interface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juniper.Logical_Interface'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juniper.Address_Family'),
        ),
    ]