
from cmdb.cmdb_django_filters import ServerFilter
import json

from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Server, Memory, Disk
from django.contrib.auth.mixins import LoginRequiredMixin

# 用于对类的方法进行装饰
# 它可以将函数装饰器，转换为类装饰器
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AssetView(View):
    def get(self, request):
        return HttpResponse('a')

    def post(self, request):
        data = request.body                 # 服务端或获取到客户端发的数据   二进制
        data = str(data, encoding='utf-8')          # 转换字符串
        data = json.loads(data)             # 对数据进行反序列化

        server_list = {**data["cpu"], **data["base"]}
        try:
            obj = Server.objects.create(**server_list)
        except Exception as e:
            print(e)

        mem_list = data["memory"]
        for keys, vals in mem_list.items():
            vals.update(server=obj)
            print(vals)
            Memory.objects.create(**vals)

        disk_list = data["disk"]
        for keys, vals in disk_list.items():
            vals.update(server=obj)
            print(vals)
            Disk.objects.create(**vals)

        return HttpResponse("post请求")


@method_decorator(csrf_exempt, name='dispatch')
class ServerListView(LoginRequiredMixin, View):
    def get(self, request):
        server_list = []
        server_list = Server.objects.values()
        print(server_list)
        return render(request, "cmdb/server_list.html", context={"server_list": server_list})


@method_decorator(csrf_exempt, name='dispatch')
class MemListView(LoginRequiredMixin, View):
    def get(self, request):
        f = ServerFilter(request.GET, queryset=Server.objects.all())
        mem_list = []
        mem_list = Memory.objects.values()
        print(mem_list)
        return render(request, "cmdb/mem_list.html", {"mem_list": mem_list, "filter": f})


@method_decorator(csrf_exempt, name='dispatch')
class DiskListView(LoginRequiredMixin, View):
    def get(self, request):
        disk_list = []
        disk_list = Disk.objects.values()
        print(disk_list)
        return render(request, "cmdb/disk_list.html", {"disk_list": disk_list})


def server_list(request):
    f = ServerFilter(request.GET, queryset=Server.objects.all())
    return render(request, 'cmdb/server_list.html', {"filter": f})
