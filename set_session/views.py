from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import HttpResponse


class SetSession(View):
    
    def get(self, request):
        self.request.session['name'] = 'django'
        return HttpResponse('SetSession')
