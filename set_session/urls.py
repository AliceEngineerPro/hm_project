# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/12 3:15
"""

import os, sys
from django.urls.conf import re_path
from set_session import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(route=r'^set_session/$', view=csrf_exempt(views.SetSession.as_view()), name='set_session'),
    re_path(route=r'^get_session/$', view=csrf_exempt(views.GetSession.as_view()), name='set_session'),
    
]