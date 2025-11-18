from django.shortcuts import render

from library.models import Book

def homepage(request):
    books = Book.objects.all() # Pega os livros do banco
    return render(request, 'bookpage.html', {'books': books})

def about(request):
    return render(request, 'about.html')

