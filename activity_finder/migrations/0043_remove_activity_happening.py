# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_finder', '0042_auto_20170830_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='happening',
        ),
    ]
