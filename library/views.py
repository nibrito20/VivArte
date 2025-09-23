from django.shortcuts import render
from .models import Book


def booklist(request):
    books = Book.objects.all().order_by('-creationdate')
    return render(request, 'library/booklist.html', { 'books': books})

def bookpage(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'library/bookpage.html', { 'book': book})

#def home(request):
#   return render(request, 'project/templates/project/home.html')