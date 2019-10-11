# 自定义过滤器
from django_filters import rest_framework as filter
from cmdb.models import Server
from users.models import UsersProfile


class ServerFilter(filter.FilterSet):
    # cpu_cores_min = filter.NumberFilter(
    #     field_name="cpu_cores", lookup_expr="gte", label="单颗CPU核心数大于")
    # cpu_cores_max = filter.NumberFilter(
    #     field_name="cpu_cores", lookup_expr="lte", label="单颗CPU核心数大于")
    cpu_cores = filter.RangeFilter(label="单颗cpu核心数的范围")  # RangeFilter  范围匹配
    host_name = filter.CharFilter(label="主机名", lookup_expr="icontains")  # 模糊匹配

    class Meta:
        model = Server
        # fields=["cpu_cores_min","cpu_cores_max"]
        fields = ["cpu_cores", "host_name"]


class UsersFilter(filter.FilterSet):
    username = filter.CharFilter(
        label="用户名", field_name="username", lookup_expr="icontains")
    class Meta:
        model=UsersProfile
        fields=["username"]
