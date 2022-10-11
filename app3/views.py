from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.views import View
from django.http.request import HttpRequest


class Index(View):
    
    def get(self, request):
        name = self.request.GET.get('name')
        return HttpResponse(f'ok{name}')


