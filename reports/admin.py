from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'crime_type', 'state', 'lga', 'status', 'reporter', 'created_at')
    list_filter = ('crime_type', 'status', 'state')
    search_fields = ('title', 'incident_description', 'location_description', 'lga')
    readonly_fields = ('created_at', 'updated_at')
