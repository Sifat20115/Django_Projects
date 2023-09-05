from django import forms
from .models import blogs
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.decorators import login_required

class blogsform(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ['blog_title', 'slug', 'images', 'description', 'category']