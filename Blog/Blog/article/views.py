from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from dbsqlite.models import ArticleProfile, Authors
from django.views import View
from .zidingyiFrom import article_addFrom
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse


# class article_detailView(View):
#     def get(self, request, id):
#         obj = ArticleProfile.objects.filter(id=id)
#         hits = obj[0].hits
#         obj.update(hits=hits+1)
#         return render(request, "article/article_detail.html", {"article_detail": obj[0]})

class article_detailView(DetailView):
    template_name = "article/article_detail.html"
    context_object_name = "article_detail"

    def get_queryset(self):
        pk = self.kwargs["pk"]
        obj = ArticleProfile.objects.filter(id=pk)  # 获取到具体对象
        hits = obj[0].hits  # 将热度用变量存储起来
        obj.update(hits=hits+1)  # 修改数据库的值
        return ArticleProfile.objects.all()  # 返回的是一个queryset对象   源码内会自己进行filter过滤


class article_addView(View):
    def get(self, request):
        return render(request, "article/article_add.html")


class article_postView(View):

    def post(self, request, username):
        title = request.POST.get("title")
        content = request.POST.get("content")
        obj = Authors.objects.filter(username=username)
        if not obj:
            username = request.user.username
            age = request.user.age
            Authors.objects.create(username=username, age=age)
        obj = Authors.objects.filter(username=username)
        ArticleProfile.objects.create(
            title=title, content=content, author=obj.first())
        return redirect(reverse("index"))


class article_delView(View):
    def get(self, request, uid):
        ArticleProfile.objects.filter(id=uid).delete()
        return redirect(reverse_lazy("users:user_center"))
