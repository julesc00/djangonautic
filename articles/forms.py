from django import forms

from . import models

class CreateArticle(forms.ModelForm):
    """Create a form for users to create articles"""
    class Meta:
        model = models.Article
        fields = ["title", "body", "slug", "thumb"]