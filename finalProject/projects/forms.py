from django import forms

from finalProject.projects.models import Project


class ProjectBaseForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('user',)

class ProjectAddForm(ProjectBaseForm):
    pass

class ProjectEditForm(ProjectBaseForm):
    class Meta:
        model = Project
        exclude = ('name', 'picture')

class ProjectDeleteForm(ProjectBaseForm):
    pass
