from django.contrib import admin

from finalProject.professionals.models import Professional


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'occupation')
    search_fields = ('name', 'email', 'phone_number', 'occupation')
    list_filter = ('name', 'occupation', 'number_of_projects')
