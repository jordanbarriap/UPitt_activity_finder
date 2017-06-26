# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_finder', '0009_auto_20170626_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people_in_charge', related_query_name='people_in_charge', to='activity_finder.People'),
        ),
    ]
