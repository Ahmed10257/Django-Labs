from django.shortcuts import redirect, render
from django.urls import path
from django.http import HttpResponse
# Create your views here.

#List of books
Books = [
    {
        'id': '1',
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'price': 7.99,
        'rating': '4.5/5',
    },
    {
        'id': '2',
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'price': 6.99,
        'rating': '4.8/5',
    },
    {
        'id': '3',
        'title': '1984',
        'author': 'George Orwell',
        'price': 9.99,
        'rating': '4.6/5',
    },
    {
        'id': '4',
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'price': 5.99,
        'rating': '4.3/5',
    },
    {
        'id': '5',
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'price': 8.99,
        'rating': '4.2/5',
    },
]

#View all books
def view_books(request):
    context = {
        'books': Books
    }   
    return render(request, 'Bookstore.html', context)

#View the details of a book by title
def book_detail(request, title):
    book = next(book for book in Books if book['title'] == title)
    return render(request, 'BookDetails.html', {'book': book})


#Delete a book by title
def delete_book(request, title):
    book = next(book for book in Books if book['title'] == title)
    Books.remove(book)
    return redirect('Home Page')

#Add a new pre-defined book
def add_book(request):
    new_book = {
        'id': '7',
        'title': 'The Picture',
        'author': 'Oscar Wilde',
        'price': 7.99,
        'rating': '4.7/5',
    }
    Books.append(new_book)
    return redirect('Home Page')

#Update the price of a book using the title
def edit_book(request, title):
    book = next(book for book in Books if book['title'] == title)
    book['price'] = 10.99
    return redirect('Home Page')

