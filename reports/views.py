# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from activity_finder.models import Activity

def activity_finder(request):
    activities=Activity.objects.all()
    return render(request, 'reports.html', {})