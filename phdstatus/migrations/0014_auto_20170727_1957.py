# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phdstatus', '0013_auto_20170727_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phd_status',
            name='details',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='t_details', to='phdstatus.T_details'),
        ),
    ]
