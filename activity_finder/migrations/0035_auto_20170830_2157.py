# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_finder', '0034_auto_20170830_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='activitytype',
            options={'verbose_name_plural': 'Activity Types'},
        ),
        migrations.AlterModelOptions(
            name='communitypartner',
            options={'verbose_name_plural': 'Community Partners'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='focusarea',
            options={'verbose_name_plural': 'Focus Areas'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='peopletype',
            options={'verbose_name_plural': 'People Types'},
        ),
        migrations.AlterModelOptions(
            name='population',
            options={'verbose_name_plural': 'Populations'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name_plural': 'Schools'},
        ),
    ]
