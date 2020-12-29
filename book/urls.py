"""
@Author: Time
@Time: 2020-11-04
"""
from django.urls import path
import book.views


urlpatterns = [

    path('addBook/', book.views.AddBook.as_view()),
    path('searchBook/', book.views.SearchBook.as_view()),
    path('deleteBook/', book.views.DeleteBook.as_view()),
    path('alterBook/', book.views.AlterBook.as_view()),
]