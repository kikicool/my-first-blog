from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)