# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
#from activity_finder.models import Activity

from django.apps import apps

def reports(request):
    entities = apps.get_app_config('activity_finder').get_models(include_auto_created=False)
    entities_list = []
    for entity in entities:
        entities_list.append(entity.__name__)
    return render(request, 'reports.html', {'entities':entities_list})