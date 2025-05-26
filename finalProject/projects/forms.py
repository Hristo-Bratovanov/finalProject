from django.forms import ModelForm, TextInput

from finalProject.projects.models import Project


class ProjectBaseForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'project_photo']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'location': TextInput(attrs={'placeholder': 'Location'}),
        }

        labels = {
            'name': "Project Name",
            'location': 'Project Location',
        }

class ProjectAddForm(ProjectBaseForm):
    pass

class ProjectEditForm(ProjectBaseForm):
    pass

class ProjectDeleteForm(ProjectBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
