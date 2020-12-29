from django.contrib import admin

# Register your models here.
# 注册模型
from borrow.models import BorrowInfo

admin.site.register(BorrowInfo)
