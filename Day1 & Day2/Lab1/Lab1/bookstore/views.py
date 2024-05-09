from django.shortcuts import redirect, render
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Book
# Create your views here.

#View all books
def view_books(request):
    Books = Book.objects.all()
    context = {
        'books': Books
    }   
    return render(request, 'Bookstore.html', context)

#View the details of a book by title
def book_detail(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'BookDetails.html', context)


#Delete a book by title
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('Home Page')

#Add a new pre-defined book
def add_book(request):
    if request.method == 'POST':
        book=Book()
        book = Book(title=request.POST.get('title'), author=request.POST.get('author'), price=request.POST.get('price'))
        book.save()
        return redirect('Home Page')
    return render(request, 'AddBook.html')

#Update the  book using the id
def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.price = request.POST.get('price')
        book.author = request.POST.get('author')
        book.title = request.POST.get('title')
        book.save()
        return redirect('Home Page')
    return render(request, 'EditBook.html', {'book': book})

