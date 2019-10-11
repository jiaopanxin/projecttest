from extra_apps import xadmin
from django.urls import path, include, re_path
from . import views

app_name = "article"

urlpatterns = [
    # path('article_content/<slug:pk>/',views.article_detailView.as_view(),name="article_content")
    path('article_content/<slug:pk>/',views.article_detailView.as_view(),name="article_content"),
    path('article_add/',views.article_addView.as_view(),name="article_add"),
    path('article_post/<username>/',views.article_postView.as_view(),name="article_post"),
    path('article_del/<uid>',views.article_delView.as_view(),name="article_del"),
]