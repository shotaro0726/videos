from django import forms
from .models import Movie, MovieComment


class MovieUploadForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'setsumei', 'samune', 'upload')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'setsumei': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'samune': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class MovieCommentCrateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MovieComment
        fields = ('name', 'text')



