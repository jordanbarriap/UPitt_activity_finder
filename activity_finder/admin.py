from django.contrib import admin
from .models import Activity,ActivityType,CommunityPartner,Course,FocusArea,Location,People,Population,School,ServedNeighbourhood,Unit

# Register your models here.
admin.site.register(Activity)
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

