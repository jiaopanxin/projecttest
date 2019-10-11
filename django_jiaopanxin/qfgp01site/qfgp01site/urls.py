"""qfgp01site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from extra_apps import xadmin
from django.urls import path, include, re_path
from users import views
from . import views as curr_views

from qfgp01site.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    path('', curr_views.index, name="index"),
    path('test/', curr_views.Test.as_view()),


    path('xadmin/', xadmin.site.urls),
    path('users/', include('users.urls'), name="users"),
    path('api/', include('api.urls'), name="api"),
    path('cmdb/', include('cmdb.urls'), name="cmdb"),
    path('cbv/', include('cbv.urls')),

]

# handler404='qfgp01site.views.page_not_found'
