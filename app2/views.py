from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse
from django.views import View
import datetime


class HomeView(View):
    
    @staticmethod
    def get(request):
        name = request.GET.get('name')
        context = {
            'name': name,
            'age': 14,
            'birthday': datetime.datetime.now(),
            'friends': ['jack', 'tom', 'rose'],
            'salary': {
                '2018': 1000,
                '2019': 5000,
                '2020': 8000,
                '2021': 12000,
                '2022': 15000
            }
        }
        return render(request, template_name='jinja2/app2/index.html', context=context)
    
    
class TemplateViewBase(View):
    
    @staticmethod
    def get(request):
        return render(request, template_name='app2/base.html')
    
    
class TemplateViewDetail(View):
    
    @staticmethod
    def get(request):
        return render(request, template_name='app2/detail.html')
