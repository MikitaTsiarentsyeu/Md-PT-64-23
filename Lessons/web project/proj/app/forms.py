from typing import Any, Dict
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=200, label="Title", help_text="title of a new post")
    content =  forms.CharField(widget=forms.Textarea(attrs={'class':"text"}))
    image = forms.ImageField()
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)

    def clean_title(self):
        title = self.cleaned_data['title']
        title = title.strip()
        if title:
            if len(title)>10:
                return title
            
        raise ValidationError("the title should consist of at least 10 symbols")
    
    def clean_content(self):
        content = str(self.cleaned_data['content'])
        content = content.strip()
        try:
            title = self.cleaned_data['title']
        except KeyError:
            return content
        if content.startswith(title):
            raise ValidationError("do not use the title as a starting of a content")
        else:
            return content
        

class AddPostModel(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'post_type')

    def clean_title(self):
        title = self.cleaned_data['title']
        title = title.strip()
        if title:
            if len(title)>10:
                return title
            
        raise ValidationError("the title should consist of at least 10 symbols")
    
    def clean_content(self):
        content = str(self.cleaned_data['content'])
        content = content.strip()
        try:
            title = self.cleaned_data['title']
        except KeyError:
            return content
        if content.startswith(title):
            raise ValidationError("do not use the title as a starting of a content")
        else:
            return content