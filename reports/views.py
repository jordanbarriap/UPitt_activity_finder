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

def get_entity(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EntityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    #else:
        #form = NameForm()

    return render(request, 'name.html', {'form': form})