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
from django.urls import path, include
from users import views
from . import views as curr_views

app_name = "cbv"
urlpatterns = [
    path('serverList/', curr_views.ServerListView.as_view(), name="serverList"),
    # path('serverList/', curr_views.ServerDListView.as_view(), name="serverList"),

    path('serverList/<int:sid>/',
         curr_views.ServerDListView.as_view(), name="serverList"),
    path('serverNowList/', curr_views.ServerNowListView.as_view(),
         name="serverNowList"),

    path('serverDList/',
         curr_views.ServerDListView.as_view(), name="serverDList"),

    path('serverDetail/<slug:pk>/', curr_views.ServerDetailView.as_view(),
         name="serverDetail")
]

# handler404='qfgp01site.views.page_not_found'
