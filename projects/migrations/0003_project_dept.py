# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-01 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170801_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dept',
            field=models.CharField(default='Computer Science', max_length=50, verbose_name='Department'),
            preserve_default=False,
        ),
    ]
