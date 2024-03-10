from django import forms
from news.models import Post,Comments


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title","text","tags")


class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=("text",)