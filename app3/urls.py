# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/9 13:12
"""

from django.urls.conf import re_path
from app3 import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^index/$',csrf_exempt(views.Index.as_view()), name='index')
]
