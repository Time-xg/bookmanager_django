from django.db import models

# Create your models here.
from book.models import BookInfo
from user.models import UserInfo


class BorrowInfo(models.Model):

    user_name = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    user = models.ForeignKey(UserInfo, verbose_name='user id', on_delete=models.PROTECT)
    book = models.ForeignKey(BookInfo, verbose_name='book id', on_delete=models.PROTECT)
    borrow_num = models.IntegerField()
    borrow_time = models.DateField()
    fines = models.CharField(max_length=10)

