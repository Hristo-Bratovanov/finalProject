from django.contrib import admin

from project_pictures.models import ProjectPicture


@admin.register(ProjectPicture)
class ProjectPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_projects')
    ordering = ('-date_of_publication',)

    @staticmethod
    def get_tagged_projects(obj):
        return ', '.join(str(pro) for pro in obj.project.all())

