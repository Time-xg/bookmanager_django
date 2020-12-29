from django.urls import path
import borrow.views


urlpatterns = [

    path('borrowBook/', borrow.views.BorrowBook.as_view()),
    path('returnBook/', borrow.views.ReturnBook.as_view()),
    path('continueBorrow/', borrow.views.ContinueBorrow.as_view()),

]