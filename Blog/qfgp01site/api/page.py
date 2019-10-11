from rest_framework.pagination import PageNumberPagination

class LimitPage(PageNumberPagination):
    page_size=2  #最大条数
    page_size_query_param= "page-size"   #前端设置的一页最大条数
    page_query_param='page'              # 前端控制这是第几页
    max_page_size=3
    