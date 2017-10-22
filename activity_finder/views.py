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
        # print("location: ",location.activities)

    data['activitytypes']=ActivityType.objects.all()

    data['communitypartners'] = CommunityPartner.objects.all()

    data['populations_served'] = PopulationServed.objects.all()
    data['focusareas'] = FocusArea.objects.all()
    # for partner in data['communitypartners']:
    #     partner_id = partner.idCommunityPartner
    #     # print("partner id: "+str(partner_id))
    #     activities = Activity.objects.filter(communitypartners=partner_id)
    #     # print(activities)
    #     activities_array = []
    #     for activity in activities:
    #         activities_array.append(activity)
    #     partner.activities = activities_array
        # print("partner: ", partner.activities)

    return render(request, 'index.html', data)