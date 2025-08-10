from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'years_of_experience',)
    ordering = ('employee_name',)
