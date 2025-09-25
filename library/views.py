from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Wishlist
from django.contrib.auth.decorators import login_required
# importar usuarios from users.migrations


def booklist(request):
    books = Book.objects.all().order_by('-creationdate')
    return render(request, 'booklist.html', { 'books': books})

def bookpage(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'bookpage.html', { 'book': book})

def addbook(request):
    return render(request, 'addbook.html', {})

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).order_by('-added_at')
    wished_books = [item.book for item in wishlist_items]
    context = {
        'wished': wished_books
    }
    return render(request, 'wishlist.html', context)

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if not Wishlist.objects.filter(user=request.user, book=book).exists(): #vê se o livro tá na lista
        Wishlist.objects.create(user=request.user, book=book)
    return redirect('library:list')

@login_required
def remove_from_wishlist(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, book=book)
            wishlist_item.delete()
        except Wishlist.DoesNotExist:
            pass  # O item não está na lista, não faz nada

    return redirect('library:wishlist')
