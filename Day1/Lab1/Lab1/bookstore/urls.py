from django.urls import path
from .views import *

urlpatterns=[
    path('', view_books, name='Home Page'),
    path('book/<str:title>/', book_detail, name='Book Details'),
    path('delete/<str:title>/', delete_book, name='Delete Book'),
    path('add/', add_book, name='Add Book'),
    path('edit/<str:title>/', edit_book, name='Edit Book'),
]