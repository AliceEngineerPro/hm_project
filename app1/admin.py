from django.contrib import admin

# Register your models here.

from app1.models import BookInfo
from app1.models import MemberInfo

admin.site.register(BookInfo)
admin.site.register(MemberInfo)
