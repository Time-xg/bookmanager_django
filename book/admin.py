from django.contrib import admin

# Register your models here.
# 注册模型
from book.models import BookInfo

admin.site.register(BookInfo)
