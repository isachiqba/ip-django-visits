from django.contrib import admin
from counter.models import ObjectVisit


class ObjectVisitAdmin(admin.ModelAdmin):
    pass

admin.site.register(ObjectVisit, ObjectVisitAdmin)
