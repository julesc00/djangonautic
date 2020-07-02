from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """Parts of an article"""
    title = models.CharField(max_length=155)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        """Truncate article body to 50 characters only"""
        return self.body[:50]+"..."
