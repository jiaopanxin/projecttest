from django.test import TestCase

# Create your tests here.
cls_name = "UserCourse"

f="""user
course
add_time
"""
fields = tuple(f.split())


TPL = """
import xadmin

from .models import {cls_name}


class {cls_name}Admin(object):
    list_display = {fields}
    list_filter = {fields}
    search_fields = {fields}


xadmin.site.register({cls_name}, {cls_name}Admin)

""".format(cls_name=cls_name, fields=fields)
print(TPL)