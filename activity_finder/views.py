# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from activity_finder.models import *

def activity_finder(request):
    a={}
    a['activities']=Activity.objects.all()
    a['locations']=Location.objects.all()
    a['activitytypes']=ActivityType.objects.all()
    a['acc']='accccccccccc'
    return render(request, 'index.html', a)