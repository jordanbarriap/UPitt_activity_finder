# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import datetime
import copy
from itertools import chain
from activity_finder.models import Activity

from django.apps import apps

def reports(request):
    entities = apps.get_app_config('activity_finder').get_models(include_auto_created=False)
    entities_list = []
    for entity in entities:
        entities_list.append(entity.__name__)
    return render(request, 'reports.html', {'entities':entities_list})


def get_filters(request):
    selected_entity = request.GET.get('entity', None)
    '''act_attributes = Activity._meta.fields
    attributes = []
    for act in act_attributes:
        if type(act).__name__ != 'AutoField':
            attributes.append(act.verbose_name)
    data = {
        'filters':attributes
    }'''
    entities = apps.get_app_config('activity_finder').get_models(include_auto_created=False)
    entities_list = []
    for entity in entities:
        if entity.__name__!=selected_entity:
            entities_list.append(entity.__name__)
    data = {
        'filters': entities_list
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
    data_filters = []
    row=1
    for value in query_values:
        if len(columns)==0:
            columns = list(value.keys())
            for column in columns:
                data_types.append(type(column).__name__)
                data_filters.append("#select_filter")
            print(data_types)
        json_value={'id':row, 'data':list(value.values())}
        print(json_value)
        json_data.append(json_value)
        #print(value.values())
        row = row + 1
    data = {
        'columns':columns,
        'types':list(data_types),
        'filters':list(data_filters),
        'data':{'rows': json_data}
    }

    return JsonResponse(data)

def get_subfilters(request):
    entity1 = request.GET.get('entity1', None)
    entity2 = request.GET.get('entity2', None)
    data=[]
    #act_values=[]
    if entity1!=entity2:
        entity_model1 = apps.get_model(app_label='activity_finder', model_name=entity1)
        entity_model2 = apps.get_model(app_label='activity_finder', model_name=entity2)
        queryset1 = entity_model1.activitys.all()
        print(queryset1)
    '''if entity=='Activity':
        field_type = type(Activity._meta.get_field(field)).__name__
        if field_type=='ForeignKey':
            queryset = Activity.objects.values(field+"__name")
            act_values = [entry for entry in queryset]
        else:
            act_values = Activity.objects.values(field)'''
    #print(act_values)
    #attributes = []
    #for act in act_attributes:
    #    if type(act).__name__ != 'AutoField':
    #        attributes.append(act.verbose_name)
    #data = {
    #    'values': act_values
    #}
    return JsonResponse(data)

def get_subtable(request):
    entity1 = request.GET.get('entity1', None)
    entity2 = request.GET.get('entity2', None)

    data=[]
    queryset1=[]
    query_values = []
    data_types = []
    data_filters = []
    columns = []
    json_data = []
    row = 0
    ent1_count=0
    rows = []
    if entity1!=entity2:
        entity_model1 = apps.get_model(app_label='activity_finder', model_name=entity1)
        entity_model2 = apps.get_model(app_label='activity_finder', model_name=entity2)



        queryset1 = entity_model1.objects.all()#objects.all().prefetch_related('activity_set')

        queryvalues = []
        queryset1_values = entity_model1.objects.all().values()#[entry for entry in queryset1]
        entity2_lowercase = entity2.lower()

        for ent1 in queryset1:
            if Activity._meta.get_field(entity2_lowercase):
                queryset2 = ent1.activity_set.all()
                ent1_values = queryset1_values[ent1_count]


                for ent2 in queryset2:
                    queryset3 = getattr(ent2, entity2_lowercase+"s").all()

                    for ent3 in queryset3:

                        rows.append(copy.copy(ent1_values))
                        rows[row][entity2]=str(ent3)

                        row = row + 1
                ent1_count = ent1_count + 1
            else:#it could be foreign key
                print("foreign key")

    print(rows)
    query_values = [entry for entry in rows]
    for value in query_values:
        if len(columns)==0:
            columns = list(value.keys())
            for column in columns:
                data_types.append(type(column).__name__)
                data_filters.append("#select_filter")
            print(data_types)
        json_value={'id':row, 'data':list(value.values())}

        json_data.append(json_value)
        row = row + 1
    data = {
        'columns':columns,
        'types':list(data_types),
        'filters':list(data_filters),
        'data':{'rows': json_data}
    }
    return JsonResponse(data)