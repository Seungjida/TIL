from django.shortcuts import render, redirect
from .models import Author
from .forms import BookCreateForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    create_form = BookCreateForm()

    context = {
        'author': author,
        'books' : books,
        'create_form' : create_form,
    }
    return render(request, 'libraries/detail.html', context)

def book_create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    create_form = BookCreateForm(request.POST)

    if create_form.is_valid():
        book = create_form.save(commit=False)
        book.author = author
        book.save()
        # author_pk가 아니라 author.pk.. 반환받은 새로운 걸 사용하기
        return redirect('libraries:detail', author.pk)
    
    context = {
        'author' : author,
        'books' : books,
        'create_form' : create_form,
    }
    return render(request, 'libraries/detail.html', context)