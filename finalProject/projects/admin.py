from django.contrib import admin

from finalProject.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'expenses', 'slug')
