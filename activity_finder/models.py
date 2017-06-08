from django.db import models


class ActivityType(models.Model):
    idActivityType = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class People(models.Model):
    idPeople = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    type = models.CharField(max_length=45)


class Activity(models.Model):
    idActivity = models.AutoField(primary_key=True)
    idActivityType = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    happening = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True,default='')
    outcomes = models.CharField(max_length=2000)
    funding = models.CharField(max_length=500)
    reviewed = models.CharField(max_length=100)
    unitNotes = models.CharField(max_length=500)
    idPeople = models.ForeignKey(People, on_delete=models.CASCADE,related_name="in_charge_person")
    universityLeaders = models.ManyToManyField(People,related_name="university_leader")


class FocusArea(models.Model):
    idFocusArea = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    activities = models.ManyToManyField(Activity)


class Location(models.Model):
    idLocation = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    activities = models.ManyToManyField(Activity)


class School(models.Model):
    idSchool = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Unit(models.Model):
    idUnit = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    idSchool = models.ForeignKey(School, on_delete=models.CASCADE)
    activities = models.ManyToManyField(Activity)


class Population(models.Model):
    idPopulation= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    activities = models.ManyToManyField(Activity)


class ServedNeighbourhood(models.Model):
    idServedNeighbourhood = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    activities = models.ManyToManyField(Activity)


class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    activities = models.ManyToManyField(Activity)


class CommunityPartner(models.Model):
    idCommunityPartner = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    activities = models.ManyToManyField(Activity)




