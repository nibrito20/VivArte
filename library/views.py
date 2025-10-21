from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Wishlist, Genre, ReviewRating
from django.contrib.auth.decorators import login_required
from .forms import reviewForm
# importar usuarios from users.migrations


def booklist(request, genero_slug=None):
    genero_atual = None
    todos_generos = Genre.objects.all()
    if genero_slug:
        genero_atual = get_object_or_404(Genre, slug=genero_slug)
        
        books = Book.objects.filter(generos__in=[genero_atual]).order_by('-creationdate')
    else:
        books = Book.objects.all().order_by('-creationdate')
    context = {
        'books': books,
        'todos_generos': todos_generos,
        'genero_atual': genero_atual
    }
    return render(request, 'booklist.html', context)


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

@login_required
def submit_review(request, book_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(book__id=book_id)
            form = reviewForm(request.POST, instance=reviews)
            form.save()
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = reviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.book_id = book_id
                data.user = request.user
                data.save()
                return redirect(url)