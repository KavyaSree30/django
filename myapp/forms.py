# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']  # Adjust fields as per your BlogPost model

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']  # Adjust fields as per your Comment model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
