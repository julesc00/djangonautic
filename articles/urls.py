from django.urls import path

from . import views

# app_name = articles (just in case in the future I have named urls that are equal.

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('<slug:slug>/', views.article_detail, name="article_detail"),
]
