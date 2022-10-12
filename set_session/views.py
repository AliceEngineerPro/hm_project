from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import HttpResponse


class SetSession(View):
    
    def get(self, request):
        # 默认session时间为14天
        self.request.session['name'] = 'django'
        # 设置session过期时间
        # self.request.session.set_expiry(7 * 24 * 3600)
        return HttpResponse('SetSession')


class GetSession(View):
    
    def get(self, request):
        name = self.request.session.get('name')
        return HttpResponse(f'{name}')
