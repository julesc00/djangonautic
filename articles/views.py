from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Article


def article_list(request):
    """List current articles"""
    articles = Article.objects.all().order_by("-date")

    return render(request, "articles/article_list.html", {"articles": articles})

@login_required(login_url="/accounts/login/")
def article_create(request):
    """Create a new article"""
    return render(request, "articles/article_create.html")

def article_detail(request, slug):
    """Show a slug specific article"""
    article = Article.objects.get(slug=slug)

    return render(request, "articles/article_detail.html", {"article":article})
