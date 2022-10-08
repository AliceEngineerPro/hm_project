# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/9 13:00
"""

from django.urls import path
from app1 import views
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^testing_render/$', views.testing_render, name='testing_render'),
    re_path(r'^testing_response/$', views.testing_response, name='testing_response'),
    re_path(r'^testing_json/$', views.testing_json, name='testing_json'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^add/$', views.add_book_info, name='add'),
    re_path(r'^update/$', views.update_book_info, name='update'),
    re_path(r'^del/$', views.del_book_info, name='del'),
    re_path(r'^is_del/$', views.is_del_book_info, name='is_del'),
    re_path(r'^books/$', views.query_book_info, name='query_book_all'),
    re_path(r'^member/$', views.query_member_info, name='query_member_info'),
    re_path(r'^jump_page_testing/$', views.jump_page_testing, name='jump_page_testing'),
    re_path(r'^book/$', views.book_info_get, name='book_info_get'),
    
    re_path(r'^center/$', csrf_exempt(views.CenterView.as_view()), name='center')

]
