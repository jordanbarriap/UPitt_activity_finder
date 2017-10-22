# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from activity_finder.models import *

def activity_finder(request):
    data={}
    data['activities']=Activity.objects.all()
    # print(data['activities'])
    data['locations']=Location.objects.all()
    #print(data['locations'])
    for location in data['locations']:
        location_id = location.idLocation
        #print("Location id: "+str(location_id))
        activities = Activity.objects.filter(locations=location_id)
        activities_array = []
        for activity in activities:
            activities_array.append(activity)
        location.activities = activities_array

    data['activitytypes']=ActivityType.objects.all()

    return render(request, 'index.html', data)