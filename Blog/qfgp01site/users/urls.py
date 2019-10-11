from . import views, converters
from django.urls import path, register_converter, re_path


register_converter(converters.FourDigitYearConverter, 'yyyy')
# 注册自定义转换类  并且起个名字 yyyy
app_name = "users"
urlpatterns = [
    # path('usersRegister/', views.userRegisterView.as_view(), name="usersRegister"),

    path('usersRegister/', views.userRegisterFromView.as_view(), name="usersRegister"),
    path('user_list/', views.user_list, name="user_list"),
    path('', views.user_index),
    path('user_detail/', views.user_detail, name="user_detail"),
    path('usersLogin/', views.UserLoginView.as_view(), name="usersLogin"),
    path('usersLogout/', views.UserLogoutView.as_view(), name="usersLogout"),
    path('my/', views.MyView.as_view(), name="my")


    # path('redirect/',views.redirects),
    # path('json/',views.json),
]


# urlpatterns = [
#     path('users_list/', views.users_list, name='users_list'),
#     #    path('<path:uid>/',views.users_detail),
#     re_path(r'(?P<uid>\d+)', views.users_detail,name="users_detail")
#     # re_path(r'^(?P<name>[a-zA-Z]+)/$',views.users_detail)
#     #    path('<yyyy:uid>',views.users_detail)
# ]
