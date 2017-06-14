# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 11:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('idActivity', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('happening', models.BooleanField()),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('outcomes', models.CharField(max_length=2000)),
                ('funding', models.CharField(max_length=500)),
                ('reviewed', models.CharField(max_length=100)),
                ('unitNotes', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('idActivityType', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityPartner',
            fields=[
                ('idCommunityPartner', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('idCourse', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FocusArea',
            fields=[
                ('idFocusArea', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('idLocation', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('idPeople', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('idPopulation', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('idSchool', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServedNeighbourhood',
            fields=[
                ('idServedNeighbourhood', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('idUnit', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('idSchool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_finder.School')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='communityPartners',
            field=models.ManyToManyField(related_name='associated_community_partner', to='activity_finder.CommunityPartner'),
        ),
        migrations.AddField(
            model_name='activity',
            name='courses',
            field=models.ManyToManyField(related_name='associated_course', to='activity_finder.Course'),
        ),
        migrations.AddField(
            model_name='activity',
            name='focusAreas',
            field=models.ManyToManyField(related_name='associated_focus_area', to='activity_finder.FocusArea'),
        ),
        migrations.AddField(
            model_name='activity',
            name='idActivityType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_finder.ActivityType'),
        ),
        migrations.AddField(
            model_name='activity',
            name='idPeople',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_charge_person', to='activity_finder.People'),
        ),
        migrations.AddField(
            model_name='activity',
            name='locations',
            field=models.ManyToManyField(related_name='associated_location', to='activity_finder.Location'),
        ),
        migrations.AddField(
            model_name='activity',
            name='populations',
            field=models.ManyToManyField(related_name='associated_population', to='activity_finder.Population'),
        ),
        migrations.AddField(
            model_name='activity',
            name='servedNeighbourhoods',
            field=models.ManyToManyField(related_name='associated_served_neighbourhoods', to='activity_finder.ServedNeighbourhood'),
        ),
        migrations.AddField(
            model_name='activity',
            name='units',
            field=models.ManyToManyField(related_name='associated_unit', to='activity_finder.Unit'),
        ),
        migrations.AddField(
            model_name='activity',
            name='universityLeaders',
            field=models.ManyToManyField(related_name='university_leader', to='activity_finder.People'),
        ),
    ]
