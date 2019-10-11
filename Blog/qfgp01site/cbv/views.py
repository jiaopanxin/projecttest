from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView
from django.utils import timezone
from cmdb.models import Server


class ServerListView(ListView):
    # 获取指定数据的model
    # model = Server
    queryset = Server.objects.all()
    # 实际上是 queryset=Server.objects.all()的简写
    # 指定模版中使用的变量名
    context_object_name = "serverList"
    # 指定模版名称
    template_name = "cbv/serverList.html"

# 获取动态数据


class ServerDListView(ListView):
    # model=Server

    template_name = "cbv/serverList.html"  # 模版名称
    context_object_name = "serverList"  # 上下文变量名（传到模版的变量名）

    def get_queryset(self):
        # server_id = self.kwargs["sid"]
        # print(server_id)
        #  # 获取动态数据

        server_id = self.request.GET.get('sid')
        # 获取get请求的参数    类似于  xxx/?sid=1
        return Server.objects.filter(id__gte=server_id)    # 返回queryset对象


class ServerNowListView(ListView):
    model = Server
    template_name = "cbv/serverNowList.html"
    context_object_name = "serverList"

    # 添加额外的数据
    # 相当于render内的context   上下文中可以有多个数据
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 对应的是上下文变量和模块   content={"serverList":Server.objects.all()}

        context['now'] = timezone.now()
        #  content={"serverList":Server.objects.all(), "now":timezone.now()}
        return context  # 返回这个字典


class ServerDetailView(DetailView):   # 获取到单个对象
    model = Server  
    template_name = "cbv/serverDetail.html"
    context_object_name = "server"
