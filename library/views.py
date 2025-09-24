from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Wishlist
from django.contrib.auth.decorators import login_required
# importar usuarios from users.migrations


def booklist(request):
    books = Book.objects.all().order_by('-creationdate')
    return render(request, 'booklist.html', { 'books': books})

def bookpage(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'library/bookpage.html', { 'book': book})

def addbook(request):
    return render(request, 'addbook.html', {})

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).order_by('-added_at')
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if not Wishlist.objects.filter(user=request.user, book=book).exists(): #vê se o livro tá na lista
        Wishlist.objects.create(user=request.user, book=book)
    return redirect('library:wishlist')

@login_required
def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    Wishlist.objects.filter(user=request.user, book=book).delete()
    return redirect('wishlist')
