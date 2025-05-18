from django import forms

from finalProject.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add a comment...'}),
        }

class SearchForm(forms.ModelForm):
    professional_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by professional name...',
        })
    )