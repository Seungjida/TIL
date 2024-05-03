from django.shortcuts import render,redirect
from .models import Book, Review

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    context = {
        'book' : book,
    }
    return render(request, 'libraries/detail.html', context)
