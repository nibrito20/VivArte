from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Wishlist, Genre, ReviewRating,RatingSearch
from django.contrib.auth.decorators import login_required
from .forms import reviewForm


def booklist(request, genero_slug=None, rating_slug=None):
    genero_atual = None
    aval_atual = None
    todos_generos = Genre.objects.all()
    todos_aval = RatingSearch.objects.all()

   

    if genero_slug:
        genero_atual = get_object_or_404(Genre, slug=genero_slug)
        books = Book.objects.filter(generos__in=[genero_atual]).order_by('-creationdate')
    elif rating_slug:
        aval_atual = get_object_or_404(RatingSearch, slug=rating_slug)
        books = Book.objects.filter(rating__in=[aval_atual]).order_by('-creationdate')
    else:
        books = Book.objects.all().order_by('-creationdate')

    context = {
        'books': books,
        'todos_generos': todos_generos,
        'genero_atual': genero_atual,
        'todos_aval': todos_aval,
        'aval_atual': aval_atual,
    }
    return render(request, 'booklist.html', context)


def bookpage(request, slug):
    # Substitui get() por filter().first() para evitar MultipleObjectsReturned
    book = Book.objects.filter(slug=slug).first()
    if not book:
        return render(request, '404.html', status=404)  # ou raise Http404("Livro não encontrado")
    
    return render(request, 'bookpage.html', {'book': book})


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
    if not Wishlist.objects.filter(user=request.user, book=book).exists():
        Wishlist.objects.create(user=request.user, book=book)
    return redirect('library:list')


@login_required
def remove_from_wishlist(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        Wishlist.objects.filter(user=request.user, book=book).delete()
    return redirect('library:wishlist')


@login_required
def submit_review(request, book_id):
    url = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        # Pega a review do usuário para esse livro, se existir
        review = ReviewRating.objects.filter(book__id=book_id, user=request.user).first()
        
        if review:
            # Atualiza review existente
            form = reviewForm(request.POST, instance=review)
        else:
            # Cria nova review
            form = reviewForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.book_id = book_id
            data.user = request.user
            data.save()
        
        return redirect(url)