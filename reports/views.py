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
    fields = []
    for field in entity_model._meta.get_fields():
        if type(field).__name__ != "AutoField":
            if field.is_relation:
                if field.many_to_one:
                    if field.related_model.__name__!="Activity":
                        if field.related_model.__name__=="People":
                            fields.append(field.name+"_id__first_name")
                            fields.append(field.name+"_id__last_name")
                        else:
                            fields.append(field.name + "_id__name")
                else:
                    if field.many_to_many:
                        if field.related_model.__name__ != "Activity":
                            if field.related_model.__name__=="People":
                                fields.append(field.name+"__first_name")
                                fields.append(field.name+"__last_name")
                            else:
                                fields.append(field.name + "__name")
            else:
                fields.append(field.name)

    print(fields)
    query_set = entity_model.objects.values(*fields)

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
    num_entities = int(request.GET.get('num_entities', None))
    entities = []
    for i in range(0,num_entities):
        ent = 'entity' + str(i+1)
        entity = request.GET.get(ent, None)
        entities.append(entity)
    #entity1 = request.GET.get('entity1', None)
    #entity2 = request.GET.get('entity2', None)

    data=[]
    query_values = []
    data_types = []
    data_filters = []
    columns = []
    json_data = []
    row = 0
    ent1_count=0
    rows = []

    entity_models = []
    for i in range(0,num_entities):
        print(entities[i])
        entity_model = apps.get_model(app_label='activity_finder', model_name=entities[i])
        entity_models.append(entity_model)

    #entity_model1 = apps.get_model(app_label='activity_finder', model_name=entity1)
    #entity_model2 = apps.get_model(app_label='activity_finder', model_name=entity2)

    rel_type_entities = [] #f: foreignkey, m: manytomany, n: is not a relationship
    for i in range(0,num_entities):
        rel_type_entities.append("n")
    #Check if entity1 is foreignkey or manytomany field in the table Activity
    act_fields = [field for field in Activity._meta.get_fields()]
    for act_field in act_fields:
        #print(act_field)
        if act_field.is_relation:
            print(act_field.related_model.__name__)
            print("is relation")
            for i in range(0,num_entities):
                if act_field.related_model.__name__==entities[i]:
                    print(act_field.related_model.__name__)
                    if act_field.many_to_one:
                        rel_type_entities[i]='f'
                    else:
                        if act_field.many_to_many:
                            rel_type_entities[i]='m'
    print(rel_type_entities)
    querysets = []
    queryset_values = []

    querysets.append(entity_models[0].objects.all())#objects.all().prefetch_related('activity_set')

    #ent1_fields = [field for field in entity_models[0]._meta.get_fields() if type(field).__name__!="AutoField"]
    #print(ent1_fields)
    #print("@@@@@@@@@-----@@@@@@@@@@")

    ent1_fields = []
    for field in entity_models[0]._meta.get_fields():
        if type(field).__name__ != "AutoField":
            if field.is_relation:
                if field.many_to_one:
                    if field.related_model.__name__ != "Activity":
                        if field.related_model.__name__ == "People":
                            ent1_fields.append(field.name + "_id__first_name")
                            ent1_fields.append(field.name + "_id__last_name")
                        else:
                            ent1_fields.append(field.name + "_id__name")
                else:
                    if field.many_to_many:
                        if field.related_model.__name__ != "Activity":
                            if field.related_model.__name__ == "People":
                                ent1_fields.append(field.name + "__first_name")
                                ent1_fields.append(field.name + "__last_name")
                            else:
                                ent1_fields.append(field.name + "__name")
            else:
                ent1_fields.append(field.name)

    print(ent1_fields)

    queryset_values.append(entity_models[0].objects.all().values(*ent1_fields))#[entry for entry in queryset1]


    if rel_type_entities[0] == 'm':
        for ent1 in querysets[0]:
            #querysets.append(ent1.activity_set.all())
            fields=[]
            for i in range (1,num_entities):
                if(rel_type_entities[i]=="m"):
                    fields.append(entities[i].lower()+"s__name")
                if(rel_type_entities[i]=="f"):
                    fields.append(entities[i].lower() + "_id__name")
            final_query_values=ent1.activity_set.all().values(*fields)
            for result in final_query_values:
                print(result)
                print("******")
                rows.append(copy.copy(queryset_values[0][ent1_count]))
                for field in result.keys():
                    rows[row][field]=result[field]
                row = row + 1
            print("#######")
            ent1_count = ent1_count + 1
            #ent1_values = queryset_values[1][ent1_count]

    '''        for ent2 in querysets[1]:
                for i in range (1,num_entities):
                    if rel_type_entities[entities[i]] == 'm':
                        querysets[i] = getattr(ent2, entity2_lowercase+"s").all()

                        for ent3 in queryset3:

                            rows.append(copy.copy(ent1_values))
                            rows[row][entities[1]]=str(ent3)
                            row = row + 1
                    else:

            ent1_count = ent1_count + 1
    else:#it could be foreign key
        if rel_type_entities=='f':
            for ent1 in querysets[0]:
                for i in range(1, num_entities):
                    querysets[current_ent] = ent1.activity_set.all()
                    ent1_values = queryset_values[0][ent1_count]

                    for ent2 in queryset2:
                        queryset3 = getattr(ent2, entity2_lowercase + "s").all()

                        for ent3 in queryset3:
                            rows.append(copy.copy(ent1_values))
                            rows[row][entity2] = str(ent3)

                            row = row + 1
                    ent1_count = ent1_count + 1'''

    print(rows)
    print("$$$$$$$$")
    query_values = [entry for entry in rows]
    for value in query_values:
        print(value)
        print("%%%%%%")
        #value = [entry for entry in value]
        #print(value)
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