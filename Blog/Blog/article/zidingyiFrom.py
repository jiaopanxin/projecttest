from django import forms
from dbsqlite.models import ArticleProfile


class article_addFrom(forms.ModelForm):
    class Meta:
        model=ArticleProfile
        fields=["title","content","author"]