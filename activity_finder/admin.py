from django.contrib import admin
from .models import Activity,ActivityType,CommunityPartner,Course,FocusArea,Location,People,PopulationServed,School,PeopleType

from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
#admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(CommunityPartner)
admin.site.register(Course)
admin.site.register(FocusArea)
admin.site.register(Location)
admin.site.register(PopulationServed)
admin.site.register(School)
admin.site.register(PeopleType)

#header
# admin.site.site_header = 'Pitt Activity Finder administration'
# admin.site.site_title = 'Pitt side admin'
# admin.site.index_title = 'Pitt side administration'

class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ["name","activitytype","people","contactInformation"]
    list_filter = ["activitytype"]
    list_editable = ["contactInformation"]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':100})},
    }

    search_fields = ('name',)

    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super(ActivityModelAdmin, self).get_search_results(request, queryset, search_term)
    #     try:
    #         search_term_as_int = int(search_term)
    #     except ValueError:
    #         pass
    #     else:
    #         queryset |= self.model.objects.filter(age=search_term_as_int)
    #     return queryset, use_distinct

admin.site.register(Activity, ActivityModelAdmin)

class PeopleModelAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name", "type"]
    list_display_links = ["first_name","last_name"]
    list_filter = ["type"]


admin.site.register(People, PeopleModelAdmin)

