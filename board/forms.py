# -*- coding: utf-8 -*-

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class BoardSearchForm(forms.Form):
    search_word = forms.CharField(label='검색')