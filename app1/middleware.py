# coding: utf8
""" 
@File: middleware.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/9/25 1:51
"""


class SimpleMiddleware1(object):

    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        print('before 1')
        response = self.get_response(request)
        print('after 1')
        return response
    
    
class SimpleMiddleware2(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        print('before 2')
        response = self.get_response(request)
        print('after 2')
        return response