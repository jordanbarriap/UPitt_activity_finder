from django.contrib import admin
from .models import Activity,ActivityType,CommunityPartner,Course,FocusArea,Location,People,Population,School,ServedNeighbourhood,Unit

from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
#admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(CommunityPartner)
admin.site.register(Course)
admin.site.register(FocusArea)
admin.site.register(Location)
admin.site.register(People)
admin.site.register(Population)
admin.site.register(ServedNeighbourhood)
admin.site.register(School)
admin.site.register(Unit)

class ActivityModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':''})},
        #models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':100})},
    }

admin.site.register(Activity, ActivityModelAdmin)