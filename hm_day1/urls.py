"""hm_day1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include
from django.views.generic.base import RedirectView
import app1.urls
import app2.urls
import app3.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^favicon.ico$', RedirectView.as_view(url=f'https://file.share.alicehome.ltd/pic/logo.ico')),
    re_path(r'^app1/', include((app1.urls, 'app1'), namespace='app1')),
    re_path(r'^app2/', include((app2.urls, 'app2'), namespace='app2')),
    re_path(r'^app3/', include((app3.urls, 'app3'), namespace='app3')),
]
