
import json

import requests
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


class AddBook(View):

    def post(self, request):
        params = request.POST
        isbn = params.get("ISBN")
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
                    isbn=params.get("ISBN"),
                    labels=book_info['labels'],
                    cover_url=book_info['cover_url'],
                    publish_date=abstract[2].strip(),
                )
                return HttpResponse('添加成功')
        else:
            return HttpResponse('查无书籍')

    def get(self,request):
        return HttpResponse('111')


class SearchBook(View):

    def post(self,request):
        params = request.POST
        search_content = str(params.get("content")).strip()
        books = BookInfo.objects.filter(name__contains=search_content)

        json_content = ''
        for book in books:
            book_data = model_to_dict(book)
            json_content += str(book_data)

        return JsonResponse(json.dumps(json_content, ensure_ascii=False), content_type='application/json', safe=False )

    def get(self,request):

        return HttpResponse("test")

