from django.shortcuts import render
from .models import Author, Book

# Create your views here.
def list(request):
    authors = Author.objects.all()
    context = {
        'authors' : authors,
    }
    return render(request, 'libraries/list.html', context)

def detail(request, author_pk):
    # 저자 누구의 상세정보인데?
    author = Author.objects.get(pk=author_pk)
    context = {
        'author' : author,
    }
    return render(request, 'libraries/detail.html', context)