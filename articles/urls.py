from django.urls import path

from . import views

#(just in case in the future I have named urls that are equal.
#app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('create/', views.article_create, name="article_create"),
    path('<slug:slug>/', views.article_detail, name="article_detail"),
]
