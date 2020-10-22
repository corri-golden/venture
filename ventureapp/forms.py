from django import forms
from ventureapp.models import Post



class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'location', 'date', 'text', 'upcoming')

        widgets = {
            'location': forms.TextInput(attrs={'class':'textinputclass'}),
            'date': forms.DateInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }