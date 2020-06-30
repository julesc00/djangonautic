from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Stopped on video 15 The Net Ninja

def article_list(request):
    articles = Article.objects.all().order_by("-date")

    return render(request, "articles/article_list.html", {"articles": articles})

def article_detail(request, slug):
    return HttpResponse(slug)