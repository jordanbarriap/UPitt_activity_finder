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

from django.contrib.auth.decorators import login_required

from django.db.models import Value
from django.db.models.functions import Concat


@login_required
def reports(request):
    entities = apps.get_app_config('activity_finder').get_models(include_auto_created=False)
    entities_list = []
    for entity in entities:
        entities_list.append(entity.__name__)
    return render(request, 'reports2.html', {'entities':entities_list})

@login_required
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

# @login_required
# def get_table(request):
#     entity = request.GET.get('entity', None)
#     print("Testing gettable: ",entity)
#     entity_model = apps.get_model(app_label='activity_finder', model_name=entity)
#     fields = []
#     for field in entity_model._meta.get_fields():
#         if type(field).__name__ != "AutoField" or entity_model.__name__=="Activity":
#             if field.is_relation:
#                 if field.many_to_one:
#                     # print("\nMany to one!")
#                     # print(field)
#                     if field.related_model.__name__!="Activity":
#                         if field.related_model.__name__=="People":
#                             # fields.append(field.name)
#                             fields.append(field.name+"__first_name")
#                             fields.append(field.name+"__last_name")
#                             fields.append(field.name + "_id__email")
#                         else:
#                             fields.append(field.name + "_id__name")
#                 else:
#                     if field.many_to_many:
#                         # print("\nMany to many! ")
#                         # print(field)
#                         if field.related_model.__name__ != "Activity":
#                             if field.related_model.__name__=="People":
#                                 fields.append(field.name)
#                                 fields.append(field.name+"__first_name")
#                                 fields.append(field.name+"__last_name")
#                             else:
#                                 if field.related_model.__name__ == "FocusArea":
#                                     fields.append(field.name)
#                                     fields.append(field.name + "__name")
#             else:
#                 # print("\nNo relation!")
#                 # print(field)
#                 fields.append(field.name)
#
#     # leader_model = entity_model.universityleaders.through.objects.all()
#     # print(leader_model)
#
#     # if entity_model.__name__ != "Activity":
#     #     fields.append("Activity__name")
#
#     print(fields)
#     print(entity_model)
#     query_set = entity_model.objects.values_list(*fields)
#
#     queryset_temp =[]
#     queryset_temp.append(entity_model.objects.all())
#     # print("#CHECING QUERY SET TEMP")
#     # print(queryset_temp)
#     row = 0
#     rows = []
#     if entity_model.__name__ != "Activity":
#         print("Here")
#         for ent1 in queryset_temp[0]:
#             # print("#CHECKING ENTITY")
#             # print(ent1)
#             fields_temp=["name"]
#             final_query_values=ent1.activity_set.all().values_list(*fields_temp)
#             print("\nFinal query values:")
#             print(final_query_values)
#         for result in final_query_values:
#             print(result)
#             print("******")
#             print(queryset_values[0][ent1_count])
#             rows.append(copy.copy(queryset_values[0][ent1_count]))
#             print(rows[row])
#             # print(result[result])
#             rows[row] = rows[row] + result
#             # for field in result:
#             #     rows[row]= rows[row] + result[field]
#             print(rows)
#             row = row + 1
#         print("#######")
#
#     # query_set = entity_model.objects.values(*fields)
#     print(query_set)
#     query_values = [entry for entry in query_set]
#     print("\n#QUERY VALUE")
#     print(query_values)
#     json_data = []
#     columns = []
#     data_types = []
#     data_filters = []
#     row=1
#
#     # for value in query_values:
#     #     if len(columns)==0:
#     #         columns = list(value.keys())
#     #         for column in columns:
#     #             data_types.append(type(column).__name__)
#     #             data_filters.append("#select_filter")
#     #         # print(data_types)
#     #     json_value={'id':row, 'data':list(value.values())}
#     #     print(list(value.values()))
#     #     # print(json_value)
#     #     json_data.append(json_value)
#     #     #print(value.values())
#     #     row = row + 1
#
#     if entity_model.__name__=="Activity":
#         columns = ['Name', 'Activity type', 'Description', 'Happening', 'Start date', 'End date', 'Outcomes', 'Funding', 'Unit notes', 'Contact name', 'Contact email',
#             'check', 'Reviewed', 'University leader 1 - First name', 'University leader 1 - Last name', 'University leader 2 - First name',
#            'University leader 2 - Last name', 'University leader 3 - First name', 'University leader 3 - Last name', 'Focus Area']
#         # columns = ['name', 'activitytype_id__name', 'description', 'happening', 'start_date', 'end_date', 'outcomes', 'funding', 'unitNotes', 'people__first_name',
#         #            'people__last_name', 'people_id__email', 'contactInformation', 'reviewed', 'universityleaders', 'universityleaders__first_name', 'universityleaders__last_name',
#         #             'focusareas__name']
#         query_values = AggregateFocusArea(query_values)
#         print("\n")
#         print(query_values)
#         query_values = AggregateUniLeader(query_values)
#     else:
#         columns = fields
#
#
#     # columns = fields
#
#
#     for column in columns:
#         data_types.append(type(column).__name__)
#         data_filters.append("#select_filter")
#     for value in query_values:
#         # print(value)
#         json_value={'id':row, 'data':value}
#         # print(type(value))
#         # print(value)
#         # print(json_value)
#         json_data.append(json_value)
#         # print(value.values())
#         row = row + 1
#
#     data = {
#         'columns':columns,
#         'types':list(data_types),
#         'filters':list(data_filters),
#         'data':{'rows': json_data}
#     }
#     # print("#CHECKING DATA")
#     # print(data)
#     return JsonResponse(data)

@login_required
#for applying the filter
def get_table(request):
    entity = request.GET.get('entity', None)
    print("Testing gettable: ",entity)
    entity_model = apps.get_model(app_label='activity_finder', model_name=entity)

    data=[]
    query_values = []
    data_types = []
    data_filters = []
    columns = []
    json_data = []
    row = 0
    ent1_count=0
    rows = []

    # print(rel_type_entities)
    querysets = []
    queryset_values = []

    #print("\nModel: ", entity_models[0])

    querysets.append(entity_model.objects.all())

    ent1_fields = []
    for field in entity_model._meta.get_fields():
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
                if field.name!="position":
                    ent1_fields.append(field.name)

    print("\nCheck query")
    print(ent1_fields)
    columns = ent1_fields

    # data_types.append(type(ent1_fields).__name__)
    # data_filters.append("#select_filter")

    queryset_values.append(entity_model.objects.all().values_list(*ent1_fields))#[entry for entry in queryset1]
    # print("\nCheck second", queryset_values[0])

    for ent1 in querysets[0]:
        #querysets.append(ent1.activity_set.all())
        fields=['name']
        # print("#CHECKING ENTITY")
        # print(ent1)
        final_query_values=ent1.activity_set.all().values_list(*fields)
        # print("\nFinal query values:")
        # print(final_query_values)
        for result in final_query_values:
            # print(result)
            # print("******")
            # print(queryset_values[0][ent1_count])
            rows.append(copy.copy(queryset_values[0][ent1_count]))
            # print(rows[row])
            # print(result[result])
            rows[row] = rows[row] + result
            # for field in result:
            #     rows[row]= rows[row] + result[field]
            # print(rows)
            row = row + 1
        # print("#######")
        ent1_count = ent1_count + 1
        #ent1_values = queryset_values[1][ent1_count]

    query_values = [entry for entry in rows]
    #print("\nCheck final data\n",query_values)

    columns.append('activity_name')
    # columns = fields
    for column in columns:
        data_types.append(type(column).__name__)
        data_filters.append("#select_filter")
    print(data_types)

    for value in query_values:
        json_value = {'id': row, 'data': value}
        json_data.append(json_value)
        row = row + 1

    json_data_no_repeated = [i for n, i in enumerate(json_data) if i not in json_data[n + 1:]]#delete possible duplicated rows in the query

    print("CHECKING FILTER")
    print(data_filters)

    data = {
        'columns':columns,
        'types':list(data_types),
        'filters':list(data_filters),
        'data':{'rows': json_data_no_repeated}
    }
    return JsonResponse(data)

def AggregateFocusArea(data):
    print("\n")
    flag = False
    results = []
    t = ()
    focusArea = ""
    for i in range(len(data)):
        if flag == False:
            t = data[i][:18]
            focusArea = data[i][19] +"; "
            flag = True
        else:
            if data[i][0]==data[i-1][0]:
                if data[i][18] > data[i-1][18]:
                    # print(t)
                    focusArea = focusArea + data[i][19] +"; "
                else:
                    t = t + (focusArea,)
                    results.append(t)
                    t = data[i][:18]
                    focusArea = data[i][19] + "; "
            else:
                t = t + (focusArea,)
                results.append(t)
                t = data[i][:18]
                focusArea = focusArea + data[i][19] + "; "
                # flag = False
    t = t + (focusArea,)
    results.append(t)
    return results

def AggregateUniLeader(data):
    print("\n")
    flag = False
    results = []
    t = ()
    index =0
    for i in range(len(data)):
        if flag == False:
            t = data[i][1:10]+(data[i][10]+' ' + data[i][11],)+data[i][12:15]+data[i][16:18]
            index = index +1
            flag = True
        else:
            if data[i][0]==data[i-1][0]:
                # print(data[i][0])
                if data[i][15] != data[i-1][15]:
                    # print(t)
                    t = t+data[i][16:18]
                    index = index + 1
                    # print("inside")
                    # print(t)
                # print(data[i][0])
            else:
                if index == 2:
                    t = t + ('','',)
                elif index == 1:
                    t = t + ('','','','')
                # print(data[i-1][18:])
                t = t + data[i-1][18:]
                results.append(t)
                t = data[i][1:10] + (data[i][10] + ' ' + data[i][11],) + data[i][12:15] + data[i][16:18]
                index =1
                # flag = False
    if index == 2:
        t = t + ('', '',)
    elif index == 1:
        t = t + ('', '', '', '')
    t = t+data[len(data)-1][18:]
    results.append(t)
    return results

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

@login_required
#for applying the filter
def get_subtable(request):
    num_entities = int(request.GET.get('num_entities', None))
    print("Check number of entities: ", num_entities)
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

    # print("\nModels: ", entity_models)
    rel_type_entities = [] #f: foreignkey, m: manytomany, n: is not a relationship
    for i in range(0,num_entities):
        rel_type_entities.append("n")
    #Check if entity1 is foreignkey or manytomany field in the table Activity
    act_fields = [field for field in Activity._meta.get_fields()]
    print("\nCheck act_fields\n")
    print(act_fields)
    for act_field in act_fields:
        #print(act_field)
        if act_field.is_relation:
            # print(act_field.related_model.__name__)
            # print("is relation")
            for i in range(0,num_entities):
                if act_field.related_model.__name__==entities[i]:
                    # print(act_field.related_model.__name__)
                    if act_field.many_to_one and act_field.related_model.__name__!="People":
                        rel_type_entities[i]='f'
                        # print("many to one")
                    else:
                        if act_field.many_to_many:
                            rel_type_entities[i]='m'
                            # print("many to many")
    # print(rel_type_entities)
    querysets = []
    queryset_values = []

    #print("\nModel: ", entity_models[0])

    querysets.append(entity_models[0].objects.all())
    # if entity_models[0].__name__!= "ActivityType":
    #     querysets.append(entity_models[0].objects.all())#objects.all().prefetch_related('activity_set')
    # else:
    #     querysets.append(entity_models[0].objects.values('name'))

    # print("\nCheck model 1: ")
    # print(querysets)
    # print("Pass")

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
                if field.name != "position":
                    ent1_fields.append(field.name)

    print("\nCheck query")
    print(ent1_fields)
    columns = ent1_fields

    # data_types.append(type(ent1_fields).__name__)
    # data_filters.append("#select_filter")

    queryset_values.append(entity_models[0].objects.all().values_list(*ent1_fields))#[entry for entry in queryset1]
    # print("\nCheck second", queryset_values[0])

    if rel_type_entities[0] != 'n':
        for ent1 in querysets[0]:
            #querysets.append(ent1.activity_set.all())
            fields=[]
            for i in range (1,num_entities):
                if(rel_type_entities[i]=="m"):
                    if entity_models[i].__name__!="People":
                       fields.append(entities[i].lower()+"s__name")
                    else:
                        fields.append("universityleaders__first_name")
                        fields.append("universityleaders__last_name")
                if(rel_type_entities[i]=="f"):
                    fields.append(entities[i].lower() + "_id__name")
                    print(entities[i].lower() + "_id__name")

            fields.append("name")
            print("#CHECKING ENTITY")
            print(ent1)
            final_query_values=ent1.activity_set.all().values_list(*fields)
            print("\nFinal query values:")
            print(final_query_values)


            for result in final_query_values:
                print(result)
                print("******")
                print(queryset_values[0][ent1_count])
                rows.append(copy.copy(queryset_values[0][ent1_count]))
                print(rows[row])
                # print(result[result])
                rows[row] = rows[row] + result
                # for field in result:
                #     rows[row]= rows[row] + result[field]
                print(rows)
                row = row + 1
            print("#######")
            ent1_count = ent1_count + 1
            #ent1_values = queryset_values[1][ent1_count]

    query_values = [entry for entry in rows]
    #print("\nCheck final data\n",query_values)

    print("#checking fields")
    print(fields)
    columns = columns + fields
    columns[len(columns)-1] = 'activity_name'
    print(columns)
    # columns = fields
    for column in columns:
        data_types.append(type(column).__name__)
        data_filters.append("#select_filter")
    print(data_types)

    for value in query_values:
        json_value = {'id': row, 'data': value}
        json_data.append(json_value)
        row = row + 1
    #
    # for value in query_values:
    #     if len(columns)==0:
    #         columns = list(value.keys())
    #         for column in columns:
    #             data_types.append(type(column).__name__)
    #             data_filters.append("#select_filter")
    #         print(data_types)
    #     json_value={'id':row, 'data':value}
    #
    #     json_data.append(json_value)
    #     row = row + 1

    json_data_no_repeated = [i for n, i in enumerate(json_data) if i not in json_data[n + 1:]]#delete possible duplicated rows in the query

    print("CHECKING FILTER")
    print(data_filters)

    data = {
        'columns':columns,
        'types':list(data_types),
        'filters':list(data_filters),
        'data':{'rows': json_data_no_repeated}
    }
    return JsonResponse(data)


# def get_subtable(request):
#     num_entities = int(request.GET.get('num_entities', None))
#     print("Check number of entities: ", num_entities)
#     entities = []
#     for i in range(0,num_entities):
#         ent = 'entity' + str(i+1)
#         entity = request.GET.get(ent, None)
#         entities.append(entity)
#     #entity1 = request.GET.get('entity1', None)
#     #entity2 = request.GET.get('entity2', None)
#
#     data=[]
#     query_values = []
#     data_types = []
#     data_filters = []
#     columns = []
#     json_data = []
#     row = 0
#     ent1_count=0
#     rows = []
#
#     entity_models = []
#     for i in range(0,num_entities):
#         print(entities[i])
#         entity_model = apps.get_model(app_label='activity_finder', model_name=entities[i])
#         entity_models.append(entity_model)
#
#     #entity_model1 = apps.get_model(app_label='activity_finder', model_name=entity1)
#     #entity_model2 = apps.get_model(app_label='activity_finder', model_name=entity2)
#
#     rel_type_entities = [] #f: foreignkey, m: manytomany, n: is not a relationship
#     for i in range(0,num_entities):
#         rel_type_entities.append("n")
#     #Check if entity1 is foreignkey or manytomany field in the table Activity
#     act_fields = [field for field in Activity._meta.get_fields()]
#     print("\nCheck act_fields\n")
#     print(act_fields)
#     for act_field in act_fields:
#         #print(act_field)
#         if act_field.is_relation:
#             print(act_field.related_model.__name__)
#             print("is relation")
#             for i in range(0,num_entities):
#                 if act_field.related_model.__name__==entities[i]:
#                     print(act_field.related_model.__name__)
#                     if act_field.many_to_one:
#                         rel_type_entities[i]='f'
#                     else:
#                         if act_field.many_to_many:
#                             rel_type_entities[i]='m'
#     print(rel_type_entities)
#     querysets = []
#     queryset_values = []
#
#     querysets.append(entity_models[0].objects.all())#objects.all().prefetch_related('activity_set')
#
#     #ent1_fields = [field for field in entity_models[0]._meta.get_fields() if type(field).__name__!="AutoField"]
#     #print(ent1_fields)
#     #print("@@@@@@@@@-----@@@@@@@@@@")
#
#     ent1_fields = []
#     for field in entity_models[0]._meta.get_fields():
#         if type(field).__name__ != "AutoField":
#             if field.is_relation:
#                 if field.many_to_one:
#                     if field.related_model.__name__ != "Activity":
#                         if field.related_model.__name__ == "People":
#                             ent1_fields.append(field.name + "_id__first_name")
#                             ent1_fields.append(field.name + "_id__last_name")
#                         else:
#                             ent1_fields.append(field.name + "_id__name")
#                 else:
#                     if field.many_to_many:
#                         if field.related_model.__name__ != "Activity":
#                             if field.related_model.__name__ == "People":
#                                 ent1_fields.append(field.name + "__first_name")
#                                 ent1_fields.append(field.name + "__last_name")
#                             else:
#                                 ent1_fields.append(field.name + "__name")
#             else:
#                 ent1_fields.append(field.name)
#
#     print(ent1_fields)
#
#     queryset_values.append(entity_models[0].objects.all().values(*ent1_fields))#[entry for entry in queryset1]
#
#
#     if rel_type_entities[0] == 'm':
#         for ent1 in querysets[0]:
#             #querysets.append(ent1.activity_set.all())
#             fields=[]
#             for i in range (1,num_entities):
#                 if(rel_type_entities[i]=="m"):
#                     fields.append(entities[i].lower()+"s__name")
#                 if(rel_type_entities[i]=="f"):
#                     fields.append(entities[i].lower() + "_id__name")
#             final_query_values=ent1.activity_set.all().values(*fields)
#             for result in final_query_values:
#                 print(result)
#                 print("******")
#                 rows.append(copy.copy(queryset_values[0][ent1_count]))
#                 for field in result.keys():
#                     rows[row][field]=result[field]
#                 row = row + 1
#             print("#######")
#             ent1_count = ent1_count + 1
#             #ent1_values = queryset_values[1][ent1_count]
#
#     '''        for ent2 in querysets[1]:
#                 for i in range (1,num_entities):
#                     if rel_type_entities[entities[i]] == 'm':
#                         querysets[i] = getattr(ent2, entity2_lowercase+"s").all()
#
#                         for ent3 in queryset3:
#
#                             rows.append(copy.copy(ent1_values))
#                             rows[row][entities[1]]=str(ent3)
#                             row = row + 1
#                     else:
#
#             ent1_count = ent1_count + 1
#     else:#it could be foreign key
#         if rel_type_entities=='f':
#             for ent1 in querysets[0]:
#                 for i in range(1, num_entities):
#                     querysets[current_ent] = ent1.activity_set.all()
#                     ent1_values = queryset_values[0][ent1_count]
#
#                     for ent2 in queryset2:
#                         queryset3 = getattr(ent2, entity2_lowercase + "s").all()
#
#                         for ent3 in queryset3:
#                             rows.append(copy.copy(ent1_values))
#                             rows[row][entity2] = str(ent3)
#
#                             row = row + 1
#                     ent1_count = ent1_count + 1'''
#
#     query_values = [entry for entry in rows]
#     for value in query_values:
#         if len(columns)==0:
#             columns = list(value.keys())
#             for column in columns:
#                 data_types.append(type(column).__name__)
#                 data_filters.append("#select_filter")
#             print(data_types)
#         json_value={'id':row, 'data':list(value.values())}
#
#         json_data.append(json_value)
#         row = row + 1
#
#     json_data_no_repeated = [i for n, i in enumerate(json_data) if i not in json_data[n + 1:]]#delete possible duplicated rows in the query
#
#     data = {
#         'columns':columns,
#         'types':list(data_types),
#         'filters':list(data_filters),
#         'data':{'rows': json_data_no_repeated}
#     }
#     return JsonResponse(data)

