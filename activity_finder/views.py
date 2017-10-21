# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from activity_finder.models import *

def activity_finder(request):
    data={}
    data['activities']=Activity.objects.all()
    data['locations']=Location.objects.all()
    print(data['locations'])
    data['activitytypes']=ActivityType.objects.all()

    return render(request, 'index.html', data)