from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views import View
from django.http import JsonResponse

from users.models import UsersProfile
from cmdb.models import Server


# JsonResponse转换的是数据库values的对象  QuerySet对象内是多个数据字典
class jsontojson(View):
    def get(self, request):
        user = Server.objects.values()  # 这是一个QuerySet对象
        # 列表嵌套字典的话需要加上safe=False这个参数
        return JsonResponse(list(user), safe=False)


# Jserializers转换的是数据库all的对象    QuerySet对象内是多个数据对象

class serializetojson(View):
    def get(self, request):
        user = UsersProfile.objects.all()
        data = serializers.serialize('json', user)
        return HttpResponse(data)


class JSONJQuery(View):
    def get(self, request):
        return render(request, 'api/JQuery.html')
