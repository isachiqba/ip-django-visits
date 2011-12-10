from django.contrib import admin
from visits.models import ObjectVisit


class ObjectVisitAdmin(admin.ModelAdmin):
    pass

admin.site.register(ObjectVisit, ObjectVisitAdmin)
