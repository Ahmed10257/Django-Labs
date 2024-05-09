from django.urls import path
from .views import *

urlpatterns=[
    path('', view_books, name='Home Page'),
    path('book/<int:id>/', book_detail, name='Book Details'),
    path('delete/<int:id>/', delete_book, name='Delete Book'),
    path('add/', add_book, name='Add Book'),
    path('edit/<int:id>/', edit_book, name='Edit Book'),
]