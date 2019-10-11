from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from users.UserRegisterForm import MyForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import FormView
from django.views import View
from django import forms
from django.urls import reverse, reverse_lazy
from users.models import UsersProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin  # CBV使用的对未登陆用户进行限制
from django.contrib.auth.decorators import login_required  # FBV限制未登陆用户访问

from users.UserRegisterForm import RegiterUserForm, UserRegisterFrom

# 登陆CBV


class UserLoginView(LoginView):
    template_name = "users/登陆框.HTML"
    # 指定一个用于接受到GET请求时，返回的模版文件

# 退出


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("index")


class userRegisterFromView(FormView):
    template_name = "users/register.html"  # get 跳转的页面
    success_url = reverse_lazy("users:usersLogin")
    # 注册成功跳转的页面
    form_class = UserRegisterFrom

    def form_valid(self, form):
        # 存入数据库方式一
        # from django.contrib.auth.hashers import make_password
        # pwd_md5=make_password(form.cleaned_data['password'])
        # form.cleaned_data['password']=pwd_md5
        # UsersProfile.objects.create(**form.cleaned_data)

        # 存入数据库方式二
        user = UsersProfile(**form.cleaned_data)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class userRegisterView(View):
    def get(self, request):
        form = RegiterUserForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        # 将用户定义的数据和自己定义的forms类中的规则进行匹配
        form = RegiterUserForm(request.POST)

        # 如果两者能够匹配成功
        if form.is_valid():

            import json
            # 输出用户输入的数据
            return HttpResponse(json.dumps(form.cleaned_data))

        # 匹配失败，返回登陆界面  继续登陆
        else:
            return render(request, "users/register.html", {"form": form})
            # form  传给前端的是一个简易的html


@login_required
def user_list(request):
    data = [
        {"id": 1001, "name": "alice", "age": 18},
        {"id": 1002, "name": "shark", "age": 19},
        {"id": 1003, "name": "root", "age": 30},
    ]
    return render(request, "users/user_list.html", context={"userList": data})


def user_index(request):
    return render(request, "users/base.HTML")


@login_required
def user_detail(request):
    return render(request, "users/user_detail.html")

#  手动与数据库匹配  ,不会自动加入到session中


def login(request):
    if request.method == "GET":
        return render(request, "users/登陆框.HTML")
    elif request.method == "POST":
        user_name = request.POST.get('user_name')  # 获取表单用户名数据
        pwd = request.POST.get('pwd')  # 获取表单密码数据
        user = UsersProfile.objects.filter(username=user_name)  # 获取到user对象
        if user:  # 如果能匹配到对应的用户名
            if user[0].check_password(pwd):  # 明文和加密密码进行比较
                return render(request, 'base.HTML')
        return render(request, "users/登陆框.HTML")
        # 视图函数中使用路由反转         模版中使用url模版标记


# def redirects(request):
#     return redirect('http://www.qfedu.com/')
# def json(request):
#     data={"name":"shark","age":18}
#     return JsonResponse(data, safe=True)


# def users_list(request):
#     username = "alice"
#     return HttpResponse(f"{username}")


# def users_detail(request, uid):
#     #    print(type(uid))
#     # print(reverse('detail'))
#     hello = "欢迎来到我的页面"
#     # print(reverse('list'))
#     return render(request, 'users_detail.html',
#         context={"userinfo": uid, "hello": hello})


class MyView(FormView):
    template_name = "users/register2.html"  # get 跳转的页面
    success_url = reverse_lazy("users:usersLogin")
    # 注册成功跳转的页面
    form_class = MyForm

    def form_valid(self, form):
        return HttpResponse(form.cleaned_data)

    def form_invalid(self, form):
        return HttpResponse('a')


# 自定义验证类
User = get_user_model()

#自定义后台登录验证
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 通过用户名或邮箱来获取用户对象
            user = User.objects.get(
                Q(username=username) |
                Q(mobile=username)
            )
            # 验证用户的密码
            if user.check_password(password):
                return user
        except Exception:
            return None
