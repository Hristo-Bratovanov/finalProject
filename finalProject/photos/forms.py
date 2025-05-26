from django import forms
from finalProject.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('user',)

class PhotoAddForm(PhotoBaseForm):
    pass

class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('photo',)

class PhotoDeleteForm(PhotoBaseForm):
    pass
