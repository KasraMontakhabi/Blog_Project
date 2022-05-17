from pyexpat import model
from django import forms
from Blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ("author", "title", "text")
        # widgets should be here
        widgets = {
            "title":forms.TextInput(attrs={"class":"textinputclass"}),
            "text": forms.Textarea(attrs={"class":"editable medium-editor-textarea postcontent"}) #the classes are CSS classes
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ("author", "text")
        widgets = {
            "author":forms.TextInput(attrs={"class":"textinputclass"}),
            "text": forms.Textarea(attrs={"class":"editable medium-editor-textarea postcontent"}) 
        }



