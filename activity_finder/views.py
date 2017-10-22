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
    # print(data['locations'])
    data['activitytypes']=CommunityPartner.objects.all()

    return render(request, 'index.html', data)