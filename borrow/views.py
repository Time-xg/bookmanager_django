import json

from django.core.serializers import serialize
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
        # book_id = params.get('bookID')
        isbn = params.get('isbn')
        days = params.get('days')
        try:
            user = UserInfo.objects.get(id=user_id)
            book = BookInfo.objects.get(isbn=isbn)
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


class Borrowfines(View):

    def post(self, request):

        params = request.POST
        user_id = params.get('userID')
        book_id = params.get('bookID')
        try:
            user = UserInfo.objects.get(id=user_id)
            book = BookInfo.objects.get(id=book_id)
        except BaseException as e:
            return HttpResponse("user or book don't existent")
        borrow_item = BorrowInfo.objects.filter(user=user, book=book)
        if borrow_item:
            borrow_num = borrow_item[0].borrow_num
            borrow_date = borrow_item[0].borrow_time
            cur_time = date.today()
            delta = cur_time - borrow_date
            if delta.days > borrow_num:
                fines = delta.days - borrow_num
                borrow_item.update(
                    fines=fines
                )
                return HttpResponse('Fines is ' + str(fines) + ' RMB')
            else:
                return HttpResponse('not fines')
        else:
            return HttpResponse('borrow info error')

    def get(self, request):

        borrows = BorrowInfo.objects.all()
        for borrow_item in borrows:
            borrow_date = borrow_item.borrow_time
            borrow_num = borrow_item.borrow_num
            cur_time = date.today()
            delta = cur_time - borrow_date
            if delta.days > borrow_num:
                fines = delta.days - borrow_num
                borrow_item.update(
                    fines=fines
                )
        return HttpResponse('Update fines succeed')


class PayFines(View):

    def post(self, request):
        params = request.POST
        user_id = params.get('userID')
        book_id = params.get('bookID')
        try:
            user = UserInfo.objects.get(id=user_id)
            book = BookInfo.objects.get(id=book_id)
        except BaseException as e:
            return HttpResponse("user or book don't existent")
        borrow_item = BorrowInfo.objects.filter(user=user, book=book)
        if borrow_item:
            borrow_item[0].delete()
            return HttpResponse('Pay to fines succeed')
        else:
            return HttpResponse('borrow info error')


class SearchBorrow(View):

    def post(self,request):
        pass

    def get(self,request):
        data = {}
        books = BorrowInfo.objects.all()
        data['borrows'] = json.loads(serialize('json', books))
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data
                            , content_type="application/json,charset=utf-8")
