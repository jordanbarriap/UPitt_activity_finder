from django.db import models
from datetime import date

class ActivityType(models.Model):
    idActivityType = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class People(models.Model):
    idPeople = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    type = models.CharField(max_length=45)

    def __str__(self):
        return self.first_name+" "+self.last_name


class FocusArea(models.Model):
    idFocusArea = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


class Location(models.Model):
    idLocation = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


class School(models.Model):
    idSchool = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Unit(models.Model):
    idUnit = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    idSchool = models.ForeignKey(School, on_delete=models.CASCADE)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


class Population(models.Model):
    idPopulation= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name



class ServedNeighbourhood(models.Model):
    idServedNeighbourhood = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


class CommunityPartner(models.Model):
    idCommunityPartner = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name



class Activity(models.Model):
    idActivity = models.AutoField(primary_key=True)
    idActivityType = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    happening = models.BooleanField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)
    outcomes = models.CharField(max_length=2000)
    funding = models.CharField(max_length=500)
    reviewed = models.CharField(max_length=100)
    unitNotes = models.CharField(max_length=500)
    idPeople = models.ForeignKey(People, on_delete=models.CASCADE,related_name="in_charge_person", null = True)
    universityLeaders = models.ManyToManyField(People,related_name="university_leader")
    #idFocusArea = models.ForeignKey(FocusArea, on_delete=models.CASCADE, null = True)
    focusAreas = models.ManyToManyField(FocusArea, related_name="associated_focus_area")
    #idLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null = True)
    locations = models.ManyToManyField(Location, related_name="associated_location")
    #idUnit = models.ForeignKey(Unit, on_delete=models.CASCADE, null = True)
    units = models.ManyToManyField(Unit,related_name="associated_unit")
    #idPopulation = models.ForeignKey(Population, on_delete=models.CASCADE, null = True)
    populations = models.ManyToManyField(Population, related_name="associated_population")
    #idServedNeighbourhood = models.ForeignKey(ServedNeighbourhood, on_delete=models.CASCADE, null = True)
    servedNeighbourhoods = models.ManyToManyField(ServedNeighbourhood, related_name="associated_served_neighbourhoods")
    #idCourse = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)
    courses = models.ManyToManyField(Course, related_name="associated_course")
    #idCommunityPartner = models.ForeignKey(CommunityPartner, on_delete=models.CASCADE, null = True)
    communityPartners = models.ManyToManyField(CommunityPartner, related_name="associated_community_partner")
    contactInformation = models.BooleanField()

    def __str__(self):
        return self.name




