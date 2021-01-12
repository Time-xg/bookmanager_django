
import json

import requests
from django.core.serializers import serialize
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from book.models import BookInfo


def getBookInfo(isbn):

    url = 'https://book.feelyou.top/isbn/' + isbn
    resp = requests.get(url=url)
    if resp.status_code == 200:
        book_info = json.loads(resp.text)
        return book_info
    else:
        return None


class ManualAddBook(View):

    def post(self, request):
        params = request.POST

        name = str(params.get('name')).strip()
        author = str(params.get('author')).strip()
        press = str(params.get('press')).strip()
        price = str(params.get('price')).strip()
        isbn = str(params.get('isbn')).strip()
        labels = str(params.get('labels')).strip()
        cover_url = str(params.get('cover_url')).strip()
        publish_date = str(params.get('publish_date')).strip()

        BookInfo.objects.create(
            name=name,
            author=author,
            press=press,
            price=price,
            isbn=isbn,
            labels=labels,
            cover_url=cover_url,
            publish_date=publish_date,
        )

        return HttpResponse("Add Book successful")


class AddBook(View):

    def post(self, request):
        params = request.POST
        isbn = params.get("isbn")
        book_info = getBookInfo(isbn)

        if book_info:
            abstract = str(book_info['abstract']).split('/')
            book = BookInfo.objects.filter(name=book_info['title'])
            if len(book) != 0:
                return HttpResponse('书籍已添加')
            else:
                BookInfo.objects.create(
                    name=book_info['title'],
                    author=abstract[0].strip(),
                    press=abstract[1].strip(),
                    price=abstract[3].strip(),
                    isbn=isbn,
                    labels=book_info['labels'],
                    cover_url=book_info['cover_url'],
                    publish_date=abstract[2].strip(),
                )
                return HttpResponse('Add Book successful')
        else:
            return HttpResponse("Don't this Book")

    def get(self, request):
        return HttpResponse('111')


class SearchBook(View):

    def post(self, request):
        data = {}
        params = request.POST
        search_content = str(params.get("content")).strip()
        books = BookInfo.objects.filter(name__contains=search_content)
        data['books'] = json.loads(serialize('json', books))
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data
                            , content_type="application/json,charset=utf-8")

    def get(self,request):
        data = {}
        books = BookInfo.objects.all()
        data['books'] = json.loads(serialize('json', books))
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data
                            , content_type="application/json,charset=utf-8")



class DeleteBook(View):

    def post(self,request):
        params = request.POST
        book_id = params.get('id')
        try:
            book = BookInfo.objects.get(id=book_id)
            book.delete()
            return HttpResponse("Delete Book successful")
        except BookInfo.DoesNotExist as e:
            return HttpResponse("Don't this Book")


class AlterBook(View):

    def post(self, request):
        params = request.POST
        book_id = params.get('id')
        try:
            book = BookInfo.objects.get(id=book_id)

            name = str(params.get('name')).strip()
            author = str(params.get('author')).strip()
            press = str(params.get('press')).strip()
            price = str(params.get('price')).strip()
            isbn = str(params.get('isbn')).strip()
            labels = str(params.get('labels')).strip()
            cover_url = str(params.get('cover_url')).strip()
            publish_date = str(params.get('publish_date')).strip()

            book.name = name if name else book.name
            book.author = author if author else book.author
            book.press = press if press else book.press
            book.price = price if price else book.price
            book.isbn = isbn if isbn else book.isbn
            book.labels = labels if labels else book.labels
            book.cover_url = cover_url if cover_url else book.cover_url
            book.publish_date = publish_date if publish_date else book.publish_date
            book.save()
            return HttpResponse("Alter Book successful")
        except BookInfo.DoesNotExist as e:
            return HttpResponse("Don't this Book")





