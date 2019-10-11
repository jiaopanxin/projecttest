from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import FormView
from django.views import View
from django.urls import reverse, reverse_lazy
from dbsqlite.models import UsersProfile, ArticleProfile, Authors
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from users.UserRegisterForm import UserRegisterFrom
from django.contrib.auth import get_user_model


class UserLoginView(LoginView):
    template_name = "users/登陆框.HTML"
    # 指定一个用于接受到GET请求时，返回的模版文件


# 退出
class UserLogoutView(LogoutView):
    # def get(self,request):
    #     return render(request,"index.html")
    next_page = reverse_lazy("index")

# 注册


class userRegisterFromView(FormView):
    template_name = "users/register.html"  # get 跳转的页面
    success_url = reverse_lazy("users:usersLogin")
    # 注册成功跳转的页面
    form_class = UserRegisterFrom

    def form_valid(self, form):
        user = UsersProfile(**form.cleaned_data)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


User = get_user_model()
# 自定义后台登录验证


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 通过用户名或邮箱来获取用户对象
            user = UsersProfile.objects.get(
                Q(username=username) |
                Q(mobile=username)
            )
            # 验证用户的密码
            if user.check_password(password):
                return user
        except Exception:
            return None

# 用户中心
class UserCenterView(View):
    def get(self, request):
        obj = UsersProfile.objects.filter(username=request.user.username)
        author = Authors.objects.filter(username=request.user.username).first()
        count = 0
        if author:
            count = len(author.article.all())
        return render(request, "users/center.html", {"user_info": obj[0], "count": count})


#用户的文章详情
class UserArticleView(View):
    def get(self, request, username):
        obj=Authors.objects.filter(username=username)
        artice=""
        if obj:
            artice=obj.first().article.all()
        return render(request, "users/user_artice.html", {"artice": artice})
