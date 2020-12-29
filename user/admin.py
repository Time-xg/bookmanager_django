from django.contrib import admin

# Register your models here.
# 注册模型
from user.models import UserInfo

admin.site.register(UserInfo)
