from django.contrib import admin
from visits.models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ['uri', 'object_app', 'object_model', 'object_id', 'visits']

admin.site.register(Visit, VisitAdmin)
