# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_finder', '0039_auto_20170830_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='section',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='term',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
    ]