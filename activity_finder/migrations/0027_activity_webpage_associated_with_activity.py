# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_finder', '0026_auto_20170830_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='webpage_associated_with_activity',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
