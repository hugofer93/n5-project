from django.contrib import admin

from n5project.apps.documents.models import Citation, Violation


@admin.register(Violation)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['person_id', 'vehicle_id', 'datetime', 'is_active']
    list_display_link = ['person', ]
    search_fields = ['person_id', 'vehicle_id', 'datetime']
    list_filter = ['is_active', 'datetime', 'creation_date']


@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    list_display = ['person_id', 'vehicle_id', 'datetime', 'is_active']
    list_display_link = ['person', ]
    search_fields = ['person_id', 'vehicle_id', 'datetime']
    list_filter = ['is_active', 'datetime', 'creation_date']
