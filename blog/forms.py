from django import forms
from mdeditor.fields import MDTextField
from .models import Post

"""class PostForm(forms.ModelForm):
    content = MDTextField()  # This will use the Markdown editor

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'status', 'tags', 'image')"""



class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      content = ['title', 'content']