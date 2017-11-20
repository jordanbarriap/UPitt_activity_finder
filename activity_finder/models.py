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

    class Meta:
        verbose_name_plural = "Activity Types"


class PeopleType(models.Model):
    idPeopleType = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "People Types"

class People(models.Model):
    idPeople = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=20,blank=True, null=True)
    type = models.ForeignKey(PeopleType, on_delete=models.CASCADE)
    # type = models.CharField(max_length=45)

    def __str__(self):
        return self.last_name +", "+self.first_name

    class Meta:
        verbose_name_plural = "People"
        ordering = ['last_name']


class FocusArea(models.Model):
    idFocusArea = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Focus Areas"


class Location(models.Model):

    idLocation = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100)
    position = GeopositionField()
    address = models.CharField(max_length=200, blank=True, null=True, editable=False)
    neighborhood = models.CharField(max_length=100, blank=True, null=True, editable=False)
    city = models.CharField(max_length=100, blank=True, null=True, editable=False)
    county = models.CharField(max_length=100, blank=True, null=True, editable=False)
    region = models.CharField(max_length=100, blank=True, null=True, editable=False)
    state = models.CharField(max_length=100, blank=True, null=True, editable=False)
    country = models.CharField(max_length=100, blank=True, null=True, editable=False)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return str(self.address)

    class Meta:
        verbose_name_plural = "Locations"

    def save(self, *args, **kwargs):
        REGIONS = {'Southwest PA': ['Lawrence', 'Butler', 'Armstrong', 'Indiana', 'Beaver', 'Allegheny', 'Washington',
                                    'Westmoreland', 'Greene', 'Fayette']}

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
        if len(neighborhood_data)>0:
            neighborhood = neighborhood_data[0]["long_name"]
            print("Neighborhood: "+neighborhood)
            if neighborhood:
                self.neighborhood = neighborhood

        # Extract city information
        city_data = [d for d in address_components if "locality" in d['types']]
        if len(city_data) > 0:
            city = city_data[0]["long_name"]
            print("City: " + city)
            if city:
                self.city = city

        #Extract county information
        county_data = [d for d in address_components if "administrative_area_level_2" in d['types']]
        county_name = ""
        if len(county_data)>0:
            county = county_data[0]["long_name"]
            county_name = county[:county.rfind(" ")]
            print("County: "+county_name)
            if county:
                self.county = county_name

        # Extract state information
        state_data = [d for d in address_components if "administrative_area_level_1" in d['types']]
        if len(state_data)>0:
            state = state_data[0]["long_name"]
            print("State: " + state)
            if state:
                self.state = state
                if state=="Pennsylvania":
                    county_name = county[:county.rfind(" ")]
                    print(county_name)
                    if county_name in REGIONS["Southwest PA"]:
                        self.region =  "Southwest PA"
                    else:
                        self.region = "Not Southwest PA"

        # Extract country information
        country_data = [d for d in address_components if "country" in d['types']]
        if len(country_data)>0:
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

    class Meta:
        verbose_name_plural = "Sponsoring School(s) at Pitt"
        ordering = ['name']


class PopulationServed(models.Model):
    idPopulation= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Populations Served"


class Course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    term = models.CharField(max_length=100, blank=True, null=True, help_text='E.g., Fall 17')
    department = models.CharField(max_length=100, blank=True, null=True, help_text='E.g., School of Pharmacy')
    course_id = models.CharField(max_length=100, blank=True, null=True, help_text='E.g., PHARM 5112')
    section = models.CharField(max_length=100, blank=True, null=True, help_text='E.g., 1050 (PETERSEN)')
    #activities = models.ManyToManyField(Activity)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Courses"


class CommunityPartner(models.Model):
    idCommunityPartner = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #address = models.CharField(max_length=200)
    #activities = models.ManyToManyField(Activity)
    website_address = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    location = GeopositionField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Community Partners"
        ordering = ['name']

    # def save(self, *args, **kwargs):
    #
    #     geolocator = GoogleV3(api_key="AIzaSyCPqXhtFS9Fu0-sCptEPyrl7nknrVGQD2g")
    #     self.location = geolocator.reverse(str(self.position.latitude)+","+str(self.position.longitude))
    #
    #     super(CommunityPartner,self).save(*args, **kwargs)  # Call the "real" save() method.
    # #    do_something_else()



DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

class Activity(models.Model):
    idActivity = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, verbose_name="Activity Name")
    activitytype = models.ForeignKey(ActivityType,  blank=True, null=True, on_delete=models.CASCADE, verbose_name="Activity Type", help_text="""Service-Learning Class: credit-bearing class in which students do community service or a community-based project as a means to learn course content and to meet course learning objectives.<br />
    Research Project: research project done in and/or with community.<br />
    Community Engagement Project: community-benefitting project done with community partners that is not part of a class, career learning experience, or research project.<br />
    Internship: student placement within an organization or business for the purposes of career learning.<br />
    One-time Volunteer Activity: voluntary activity – not part of a class – done by student, staff, or faculty on a one-time basis.<br />
    Ongoing Volunteer Activity: voluntary activity – not part of a class – done by student, staff, or faculty on a one-time basis.<br />
    Public Event/Workshop: event or workshop open to the public.<br />
    Consulting/Coaching.<br />
    Evaluation: measuring the impact or outcomes of a community-based program.<br />""")
    description = models.TextField(max_length=2000)
    estimated_start_date = models.DateField(default=date.today, help_text='(yyyy-mm-dd)<br />For data entry purposes, please provide a complete estimated start date including a day, month, and year, even if the day and month are unknown.')
    estimated_end_date = models.DateField(blank=True, null=True, help_text='(yyyy-mm-dd). Leave blank if currently ongoing.')
    webpage_associated_with_activity = models.CharField(max_length=500, blank=True, null=True)
    outcomes = models.TextField(max_length=2000, blank=True, null=True, help_text='Please include a description of any products, programs, or outputs this activity has generated. This information will not be publicly viewable.')
    funding = models.CharField(max_length=500, blank=True, null=True, help_text='Please include the internal (Pitt) and external sources of funding that support this activity. This information will not by publicly viewable.')
    # unitNotes = models.CharField(max_length=500, blank=True, null=True)
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="people_in_charge", null = True, verbose_name="Contact Person")
    contactInformation= models.BooleanField(help_text='Please check it if you want the contact information to be visible in public.', verbose_name='Contact Information')
    universityleaders = models.ManyToManyField(People, verbose_name='University Leader(s)')#,related_name="associated_university_leader")
    #idFocusArea = models.ForeignKey(FocusArea, on_delete=models.CASCADE, null = True)
    focusareas = models.ManyToManyField(FocusArea)#, related_name="associated_focus_area")
    #idLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null = True)
    locations = models.ManyToManyField(Location)#, related_name="associated_location")
    #idUnit = models.ForeignKey(Unit, on_delete=models.CASCADE, null = True)
    schools = models.ManyToManyField(School, blank=True, null=True)
    #idPopulation = models.ForeignKey(Population, on_delete=models.CASCADE, null = True)
    populations_served = models.ManyToManyField(PopulationServed, verbose_name='Populations Served')#, related_name="associated_population")
    #idServedNeighbourhood = models.ForeignKey(ServedNeighbourhood, on_delete=models.CASCADE, null = True)
    #idCourse = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)
    courses = models.ManyToManyField(Course, blank=True, null=True)#, related_name="associated_course")
    #idCommunityPartner = models.ForeignKey(CommunityPartner, on_delete=models.CASCADE, null = True)
    communitypartners = models.ManyToManyField(CommunityPartner, verbose_name="Community Organization Name")#, related_name="associated_community_partner")
    reviewed = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"

class MyAppModel(models.Model):
    class Meta:
        app_label = 'My App Label'
        abstract = True

