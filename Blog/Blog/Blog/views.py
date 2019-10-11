from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from dbsqlite.models import ArticleProfile
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


# def index(request):
#     ariticle = ArticleProfile.objects.order_by("-hits")[:10]
#     return render(request, "index.html", {"ariticle": ariticle})

class index(ListView):
    context_object_name = "ariticle"
    template_name = "index.html"

    def get_queryset(self):
        return ArticleProfile.objects.order_by("-hits")[:10]
