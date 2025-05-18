from django.contrib import admin

from finalProject.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'location', 'get_tagged_professionals')

    @staticmethod
    def get_tagged_professionals(obj):
        return ', '.join(str(prof) for prof in obj.professional.all())

