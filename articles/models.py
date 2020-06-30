from django.db import models


class Article(models.Model):
    """Parts of an article"""
    title = models.CharField(max_length=155)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    # add author later

    def __str__(self):
        return self.title

    def snippet(self):
        """Truncate article body to 50 characters only"""
        return self.body[:50]+"..."
