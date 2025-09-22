from django.shortcuts import render
from .models import Book

def booklist(request):
    books = Book.objects.all().order_by('-creationdate')
    return render(request, 'library/booklist.html', { 'books': books})

