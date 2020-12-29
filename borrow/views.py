from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from book.models import BookInfo
from borrow.models import BorrowInfo
from user.models import UserInfo
from datetime import date

class BorrowBook(View):

    def post(self, request):
        params = request.POST
        user_id = params.get('userID')
        book_id = params.get('bookID')
        days = params.get('days')
        try:
            user = UserInfo.objects.get(id=user_id)
            book = BookInfo.objects.get(id=book_id)
        except BaseException as e:
            return HttpResponse("user or book don't existent")

        BorrowInfo.objects.create(
            user=user,
            book=book,
            user_name=user.name,
            book_name=book.name,
            borrow_num=days,
            borrow_time=date.today(),
            fines=0,
        )
        return HttpResponse("borrow succeed")

    def get(self, request):
        pass


class ReturnBook(View):

    def post(self,request):
        params = request.POST
        user_id = params.get('userID')
        book_id = params.get('bookID')
        try:
            user = UserInfo.objects.get(id=user_id)
            book = BookInfo.objects.get(id=book_id)
        except BaseException as e:
            return HttpResponse("user or book don't existent")
        borrow_item = BorrowInfo.objects.filter(user=user,book=book)
        if borrow_item:
            borrow_item.delete()
            return HttpResponse('return book succeed')
        else:
            return HttpResponse('borrow info error')

class ContinueBorrow(View):

    def post(self,request):
        params = request.POST
        user_id = params.get('userID')
        book_id = params.get('bookID')
        days = params.get('days')
        try:
            user = UserInfo.objects.get(id=user_id)
            book = BookInfo.objects.get(id=book_id)
        except BaseException as e:
            return HttpResponse("user or book don't existent")
        borrow_item = BorrowInfo.objects.filter(user=user, book=book)
        if borrow_item:
            borrow_item.update(borrow_num=days)
            return HttpResponse('return book succeed')
        else:
            return HttpResponse('borrow info error')
