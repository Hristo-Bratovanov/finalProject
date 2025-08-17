from django.contrib import admin

from project_pictures.models import ProjectPicture


@admin.register(ProjectPicture)
class ProjectPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description',)
    ordering = ('-date_of_publication',)

