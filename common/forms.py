from django import forms
from common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add a comment...'}),
        }

class SearchForm(forms.Form):
    company_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Filter by company name...',
            }
        )
    )