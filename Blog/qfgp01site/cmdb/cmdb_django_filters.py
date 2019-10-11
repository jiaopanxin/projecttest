# 过滤

import django_filters
from .models import Server

#  简单化的过滤器
class ServerFilter(django_filters.FilterSet):
    class Meta:
        model = Server
        fields = {
            'host_name': ['exact', ],  # exact 精确查找
            # 会生成 physical_count__lt   physical_count__gt
            'physical_count': ['lt', 'gt'],
            'kernel': ['exact']
            # 'sysusers__name': ['exact']
        }
