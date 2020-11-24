from django import forms
from ventureapp.models import Post, Comment




class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'location', 'date', 'text', 'upcoming', 'post_image')

        widgets = {
            'location': forms.TextInput(attrs={'class':'textinputclass'}),
            'date': forms.DateInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class PostCommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'textinputclass'}),
            'body': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }