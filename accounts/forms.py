from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django import forms

from accounts.models import CompanyProfile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class AppUserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ('user', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'value'}),
            'last_name': forms.TextInput(attrs={'class': 'value'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'value', 'type': 'date'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'value'}),
            'email': forms.EmailInput(attrs={'class': 'value'}),
            'phone_number': forms.TextInput(attrs={'class': 'value'}),
            'occupation': forms.Select(attrs={'class': 'value'}),
            'age': forms.NumberInput(attrs={'class': 'value'}),
            'about_me': forms.Textarea(attrs={'class': 'value'}),
        }



