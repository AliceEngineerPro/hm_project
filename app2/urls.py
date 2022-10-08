# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/25 2:37
"""

from app2 import views
from django.urls.conf import re_path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(route='^home/$', view=csrf_exempt(views.HomeView.as_view()), name='home'),
    re_path(route='^base/$', view=csrf_exempt(views.TemplateViewBase.as_view()), name='base'),
    re_path(route='^detail/$', view=csrf_exempt(views.TemplateViewDetail.as_view()), name='detail')
]
