from extra_apps import xadmin
from django.urls import path, include
from api import views
from . import drf_views
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from api.drf_views import ServerViewSet

# 向路由注册视图集
router = DefaultRouter()
router.register(r'server-router', ServerViewSet)
router.register(r'user-all', drf_views.UserViewSet)
router.register(r'user-search', drf_views.UserSearchView)


app_name = "api"
urlpatterns = [
    # 过滤
    path('user-filter/', drf_views.UserFilter.as_view()),
    path('server-filter/', drf_views.ServerFilterView.as_view()),
    path('disk-filter/', drf_views.DiskFilterView.as_view()),
    path('Server-cust-filter/', drf_views.ServerCustView.as_view()),

    # 自动配置路由   路由集合
    path('', include(router.urls)),


    # 查看详情信息
    path('drf-server-detail/<int:pk>/', drf_views.ServerDetailView.as_view()),
    path('drf_users_generDetail/<int:pk>/',
         drf_views.UserSerializeDetailView.as_view()),


    # 查看用户信息
    path('drf_users_gener/', drf_views.UserGenerView.as_view()),
    path('drf_users_generList/', drf_views.UserGenerListView.as_view()),


    # APIView
    path('asset/', drf_views.ServerManyView.as_view()),
    path('drf_users_info/', drf_views.UserSerializeView.as_view()),
    path('drf_servers_info/', drf_views.ServersSerializeView.as_view()),
    path('drf_memory_info/', drf_views.MemoryGenerListView.as_view()),
    path('drf_disk_info/', drf_views.DiskSerializeView.as_view()),
    # path('drf_asset_info/', drf_views.AssetSerializeView.as_view()),
    # path('drf_sysusers_info/', drf_views.SysusersSerializeView.as_view()),



    path('user_Json1/', views.jsontojson.as_view(), name="userJson1"),
    path('user_Json2/', views.serializetojson.as_view(), name="userJson2"),
    # path('user_JQuery/', views.JSONJQuery.as_view(), name="JQuery"),
    # 当 view视图内只返回一个页面的时候 可以用TemplateView 模块   不用编写view视图
    path('JQuery/', TemplateView.as_view(template_name="api/JQuery.html"), name="JQuery"),
    path('vue/', TemplateView.as_view(template_name="api/vue-axios.html"), name="vue"),
]

# handler404='qfgp01site.views.page_not_found'
