from django.contrib import admin

from finalProject.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'description', 'get_tagged_projects')

    @staticmethod
    def get_tagged_projects(obj):
        return ', '.join(str(pro) for pro in obj.tagged_projects.all())

