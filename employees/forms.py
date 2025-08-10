from django import forms
from employees.models import Employee


class EmployeeBaseForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('user',)

class EmployeeAddForm(EmployeeBaseForm):
    pass

class EmployeeEditForm(EmployeeBaseForm):
    pass