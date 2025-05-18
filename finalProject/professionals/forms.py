from django.forms import ModelForm, TextInput, EmailInput, Select

from finalProject.professionals.models import Professional


class ProfessionalBaseForm(ModelForm):
    class Meta:
        model = Professional
        fields = ['name', 'email', 'occupation']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'occupation': Select(attrs={'placeholder': 'Occupation'}),
        }

        labels = {
            'name': "Person's Name",
            'email': 'Email',
            'occupation': 'Occupied profession',
        }

class ProfessionalAddForm(ProfessionalBaseForm):
    pass

class ProfessionalEditForm(ProfessionalBaseForm):
    pass

class ProfessionalDeleteForm(ProfessionalBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
