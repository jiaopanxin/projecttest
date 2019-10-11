import xadmin
from .models import Authors, ArticleProfile, UsersProfile


class AuthorsAdmin:
    list_display = ("username", "age")
    search_fields = ("username", "age")
    list_filter = ("username", "age")


class ArticleAdmin:
    list_display = ("title", "content",
                    "create_time", "update_time", "hits", "author")
    search_fields = ("title", "content",
                     "create_time", "update_time", "hits", "author")
    list_filter = ("title", "content",
                   "create_time", "update_time", "hits", "author")


xadmin.site.register(Authors, AuthorsAdmin)
xadmin.site.register(ArticleProfile, ArticleAdmin)
