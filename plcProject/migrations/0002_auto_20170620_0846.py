# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-20 08:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plcProject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plc_data_one',
            old_name='do',
            new_name='dO',
        ),
        migrations.RenameField(
            model_name='plc_data_one_settings',
            old_name='do',
            new_name='dO',
        ),
    ]