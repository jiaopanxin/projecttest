from .cust_filter import UsersFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from api.page import LimitPage
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .cust_filter import ServerFilter

from users.models import UsersProfile
from cmdb.models import Server, Memory, Disk, Asset, SysUsers
from api.serializer import (ServerSerialize, UserSerialize, DiskSerialize,
                            MemorySerialize, ServerSerializeMany)

# APIView


class ServerManyView(APIView):
    def get(self, request):
        server = Server.objects.all()
        server = ServerSerializeMany(server, many=True)
        return Response(server.data)


class UserSerializeView(APIView):  # 查看用户的信息
    def get(self, request):
        user = UsersProfile.objects.all()
        user = UserSerialize(user, many=True)
        return Response(user.data)


class ServersSerializeView(APIView):
    def get(self, request):
        server = Server.objects.all()
        server = ServerSerialize(server, many=True)
        return Response(server.data)


class DiskSerializeView(APIView):
    def get(self, request):
        disk = Disk.objects.all()
        disk = DiskSerialize(disk, many=True)
        return Response(disk.data)


class MemorySerializeView(APIView):
    def get(self, request):
        memory = Memory.objects.all()
        memory = MemorySerialize(memory, many=True)
        return Response(memory.data)


# 查看指定用户的详情
class UserSerializeDetailView(mixins.RetrieveModelMixin,
                              generics.GenericAPIView):
    queryset = UsersProfile.objects.all()
    serializer_class = UserSerialize

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


#  查看用户信息
class UserGenerView(mixins.ListModelMixin, generics.GenericAPIView):
     # 这两个字段是GenericAPIView  中定义好的
    queryset = UsersProfile.objects.all()
    serializer_class = UserSerialize

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# 查看用户信息的优化
class UserGenerListView(generics.ListAPIView):
    """ListAPIView  直接继承了mixins.ListModelMixin, generics.GenericAPIView
    这两个     直接调用ListModelMixin的 list方法"""
    queryset = UsersProfile.objects.all()
    serializer_class = UserSerialize

# 查看内存信息


class MemoryGenerListView(generics.ListAPIView):
    """ListAPIView  直接继承了mixins.ListModelMixin, generics.GenericAPIView
    这两个     直接调用ListModelMixin的 list方法"""
    queryset = Memory.objects.all()
    serializer_class = MemorySerialize

    pagination_class = LimitPage


# 查看server的具体详情
class ServerDetailView(generics.RetrieveAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerialize

# 自动配置路由(路由集合)，查看服务的某个具体详情
#  ModelViewSet  继承mixins的增删改查   可以对其操作  只需要写一个路由


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerialize

    # pagination_class = LimitPage

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = UsersProfile.objects.all()
    serializer_class = UserSerialize


class UserFilter(generics.ListAPIView):

    serializer_class = UserSerialize

    # get方法传参
    def get_queryset(self):
        queryset = UsersProfile.objects.all()

        username = self.request.query_params.get("username", None)
        if username:
            queryset = queryset.filter(username=username)
        return queryset

    # 过滤当前用户的信息
    # def get_queryset(self):
    #     user = self.request.user
    #     return UsersProfile.objects.filter(username=user)

# 过滤


class ServerFilterView(generics.ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerialize

    filterset_fields = ["host_name", "os_name"]


class DiskFilterView(generics.ListAPIView):
    queryset = Disk.objects.all()
    serializer_class = DiskSerialize

    filterset_fields = ["slot", "type"]

# 自定义过滤器


class ServerCustView(generics.ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerialize
    filterset_class = ServerFilter


# 搜索
class UserSearchView(viewsets.ReadOnlyModelViewSet):
    queryset = UsersProfile.objects.all()
    serializer_class = UserSerialize
    # 添加后端
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["$username", "email"]  # 搜索的字段

    # 排序
    ordering_fields = ["username", "password"]  # 可以排序的字段
    ordering = ["-username"]  # 默认排序的字段

    filterset_class = UsersFilter  # 过滤的字段
