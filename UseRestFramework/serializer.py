# coding: utf8
""" 
@File: serializer.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/17 0:58
"""

import os, sys

from rest_framework import serializers


# 自定义序列化器
class BookSerializer(serializers.Serializer):
    """图书序列化"""
    
    # 定义字段
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField()
    bcomment = serializers.IntegerField()
    is_delete = serializers.BooleanField()
    

