import json

from . import views
from django.urls import path


app_name = "cmdb"
urlpatterns = [
    path('asset/', views.AssetView.as_view(), name="asset"),
    # path('serverList/', views.ServerListView.as_view(), name="serverList"),
    path('serverList/', views.server_list, name="serverList"),
    path('memList/', views.MemListView.as_view(), name="memList"),
    path('diskList/',views.DiskListView.as_view(),name="diskList")

]
