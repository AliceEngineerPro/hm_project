# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/12 13:03
"""

import os, sys
from django.urls.conf import re_path
from csrf_l import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^csrf/$', views.LoginIndex.as_view(), name='csrf')
]
