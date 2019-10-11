from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def index(request):
    return render(request, 'index.html')


def page_not_found(request, exception=None):
    return render(request, '404.html', status=404)


class Test(View):
    def get(self, request):
        return HttpResponse("aa")
