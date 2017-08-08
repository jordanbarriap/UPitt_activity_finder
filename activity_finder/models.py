from django.db import models
from datetime import date
from geoposition.fields import GeopositionField
from geopy.geocoders import GoogleV3

import pprint
import json

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
        return self.first_name + " " + self.last_name

class FocusArea(models.Model):
    idFocusArea = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name


class Location(models.Model):
    idLocation = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = GeopositionField()
    address = models.CharField(max_length=200, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        pp = pprint.PrettyPrinter()
        geolocator = GoogleV3(api_key="AIzaSyCPqXhtFS9Fu0-sCptEPyrl7nknrVGQD2g")
        location = geolocator.reverse(str(self.position.latitude)+","+str(self.position.longitude))
        address = location[0].address
        if address:
            self.address = address

        #pp.pprint(location[0].raw)

        address_components = location[0].raw["address_components"]

        # Extract neighborhood information
        neighborhood_data = [d for d in address_components if "neighborhood" in d['types']]
        neighborhood = neighborhood_data[0]["long_name"]
        print("Neighborhood: "+neighborhood)
        if neighborhood:
            self.neighborhood = neighborhood

        # Extract city information
        city_data = [d for d in address_components if "locality" in d['types']]
        city = city_data[0]["long_name"]
        print("City: " + city)
        if city:
            self.city = city

        #Extract county information
        county_data = [d for d in address_components if "administrative_area_level_2" in d['types']]
        county = county_data[0]["long_name"]
        print("County: "+county)
        if county:
            self.county = county

        #Extract region information (just for PA)

        # Extract state information
        state_data = [d for d in address_components if "administrative_area_level_1" in d['types']]
        state = state_data[0]["long_name"]
        print("State: " + state)
        if state:
            self.state = state

        # Extract country information
        country_data = [d for d in address_components if "country" in d['types']]
        country = country_data[0]["long_name"]
        print("Country: " + country)
        if country:
            self.country = country

        super(Location,self).save(*args, **kwargs)  # Call the "real" save() method.
    #    do_something_else()


class School(models.Model):
    idSchool = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Unit(models.Model):
    idUnit = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
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
    name = models.CharField(max_length=300)
    activitytype = models.ForeignKey(ActivityType, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    happening = models.BooleanField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)
    outcomes = models.TextField(max_length=2000, blank=True, null=True)
    funding = models.CharField(max_length=500, blank=True, null=True)
    unitNotes = models.CharField(max_length=500, blank=True, null=True)
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="people_in_charge", null = True)
    contactInformation= models.BooleanField()
    universityleaders = models.ManyToManyField(People)#,related_name="associated_university_leader")
    #idFocusArea = models.ForeignKey(FocusArea, on_delete=models.CASCADE, null = True)
    focusareas = models.ManyToManyField(FocusArea)#, related_name="associated_focus_area")
    #idLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null = True)
    locations = models.ManyToManyField(Location)#, related_name="associated_location")
    #idUnit = models.ForeignKey(Unit, on_delete=models.CASCADE, null = True)
    schools = models.ManyToManyField(School)
    units = models.ManyToManyField(Unit)#,related_name="associated_unit")
    #idPopulation = models.ForeignKey(Population, on_delete=models.CASCADE, null = True)
    populations = models.ManyToManyField(Population)#, related_name="associated_population")
    #idServedNeighbourhood = models.ForeignKey(ServedNeighbourhood, on_delete=models.CASCADE, null = True)
    servedneighbourhoods = models.ManyToManyField(ServedNeighbourhood)#, related_name="associated_served_neighbourhoods")
    #idCourse = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)
    courses = models.ManyToManyField(Course)#, related_name="associated_course")
    #idCommunityPartner = models.ForeignKey(CommunityPartner, on_delete=models.CASCADE, null = True)
    communitypartners = models.ManyToManyField(CommunityPartner)#, related_name="associated_community_partner")
    reviewed = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name




