from django import forms

from projects.models import Project


class ProjectBaseForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'project_photo']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        }

        labels = {
            'name': "Project Name",
            'location': 'Project Location',
        }

class ProjectAddForm(ProjectBaseForm):
    pass

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'project_photo', 'description', 'expenses']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'expenses': forms.NumberInput(attrs={'placeholder': 'Expenses'}),
        }

        labels = {
            'name': "Project Name",
            'location': 'Project Location',
            'description': 'Description',
            'expenses': 'Expenses',
        }


class ProjectDeleteForm(ProjectBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
