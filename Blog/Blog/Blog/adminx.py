from extra_apps import xadmin
from dbsqlite.models import UsersProfile, Authors, ArticleProfile


class UserAdmin:
    list_display = ('username', 'password', 'email', 'mobile', 'gender')
    search_fields = ('username', 'password', 'email', 'mobile', 'gender')
    list_filter = ('username', 'password', 'email', 'mobile', 'gender')


xadmin.site.register(UsersProfile, UserAdmin)
