from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Article
from . import forms


def article_list(request):
    """List current articles"""
    articles = Article.objects.all().order_by("-date")

    return render(request, "articles/article_list.html", {"articles": articles})

@login_required(login_url="/accounts/login/")
def article_create(request):
    """Create a new article"""
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect("article_list")
    else:
        form = forms.CreateArticle()

    return render(request, "articles/article_create.html", {"form": form})

def article_detail(request, slug):
    """Show a slug specific article"""
    article = Article.objects.get(slug=slug)

    return render(request, "articles/article_detail.html", {"article":article})
