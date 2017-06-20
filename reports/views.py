# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import datetime
from activity_finder.models import Activity

from django.apps import apps

def reports(request):
    entities = apps.get_app_config('activity_finder').get_models(include_auto_created=False)
    entities_list = []
    for entity in entities:
        entities_list.append(entity.__name__)
    return render(request, 'reports.html', {'entities':entities_list})


def get_filters(request):
    entity = request.GET.get('entity', None)
    act_attributes = Activity._meta.fields
    attributes = []
    for act in act_attributes:
        if type(act).__name__ != 'AutoField':
            attributes.append(act.verbose_name)
    data = {
        'filters':attributes
    }
    return JsonResponse(data)


def get_table(request):
    entity = request.GET.get('entity', None)
    entity_model = apps.get_model(app_label='activity_finder', model_name=entity)
    query_set = entity_model.objects.values()
    query_values = [entry for entry in query_set]
    json_data = []
    columns = []
    data_types = []
    row=1
    for value in query_values:
        if len(columns)==0:
            columns = list(value.keys())
            for column in columns:
                data_types.append(type(column).__name__)
            print(data_types)
        json_value={'id':row, 'data':list(value.values())}
        print(json_value)
        json_data.append(json_value)
        #print(value.values())
        row = row + 1
    data = {
        'columns':columns,
        'types':list(data_types),
        'data':{'rows': json_data}
    }

    return JsonResponse(data)

def get_subfilters(request):
    entity = request.GET.get('entity', None)
    field = request.GET.get('field', None)
    act_values=[]
    if entity=='Activity':
        field_type = type(Activity._meta.get_field(field)).__name__
        if field_type=='ForeignKey':
            queryset = Activity.objects.values(field+"__name")
            act_values = [entry for entry in queryset]
        else:
            act_values = Activity.objects.values(field)
    print(act_values)
    #attributes = []
    #for act in act_attributes:
    #    if type(act).__name__ != 'AutoField':
    #        attributes.append(act.verbose_name)
    data = {
        'values': act_values
    }
    return JsonResponse(data)