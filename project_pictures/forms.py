from django import forms
from project_pictures.models import ProjectPicture


class PictureBaseForm(forms.ModelForm):
    class Meta:
        model = ProjectPicture
        exclude = ('user',)

class PictureAddForm(PictureBaseForm):
    pass

class PictureEditForm(PictureBaseForm):
    class Meta(PictureBaseForm.Meta):
        exclude = PictureBaseForm.Meta.exclude + ('picture',)
