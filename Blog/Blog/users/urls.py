from . import views
from django.urls import path, register_converter, re_path
from Blog import views as blog_views

app_name = "users"
urlpatterns = [
    path('',blog_views.index),
    path('usersRegister/', views.userRegisterFromView.as_view(), name="usersRegister"),
    path('usersLogin/', views.UserLoginView.as_view(), name="usersLogin"),
    path('usersLogout/', views.UserLogoutView.as_view(), name="usersLogout"),
    path('userCenter/', views.UserCenterView.as_view(), name="user_center"),
    path('userArticle/<username>', views.UserArticleView.as_view(), name="users_article"),
]
