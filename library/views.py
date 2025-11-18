from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Wishlist, Genre, ReviewRating, RatingSearch, Carrinho
from django.contrib.auth.decorators import login_required
from .forms import reviewForm
from .models import Book

def booklist(request, genero_slug=None, rating_slug=None):
    genero_atual = None
    aval_atual = None
    todos_generos = Genre.objects.all()
    todos_aval = RatingSearch.objects.all()
    livros_destaque = Book.objects.all().order_by('-creationdate')[:5]

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
        'livros_destaque': livros_destaque,
        'todos_generos': todos_generos,
        'genero_atual': genero_atual,
        'todos_aval': todos_aval,
        'aval_atual': aval_atual,
    }
    return render(request, 'booklist.html', context)


def bookpage(request, slug):
    book = Book.objects.filter(slug=slug).first()
    if not book:
        return render(request, '404.html', status=404)
    
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
        review = ReviewRating.objects.filter(book__id=book_id, user=request.user).first()
        
        if review:
            form = reviewForm(request.POST, instance=review)
        else:
            form = reviewForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.book_id = book_id
            data.user = request.user
            data.save()
        
        return redirect(url)
    
@login_required   
def ver_carrinho(request):
    itens = Carrinho.objects.filter(user=request.user)

    total = sum(item.book.price * item.quantity for item in itens)

    context = {
        'itens': itens,
        'total': total
    }
    return render(request, 'carrinho.html', context)

@login_required
def adicionar_ao_carrinho(request, book_id):
    livro = get_object_or_404(Book, id=book_id)

    item, created = Carrinho.objects.get_or_create(
        user=request.user,
        book=livro,
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('ver_carrinho')

@login_required
def remover_item_do_carrinho(request, item_id):
    item = get_object_or_404(Carrinho, id=item_id, user=request.user)
    item.delete()
    return redirect('ver_carrinho')

def aumentar_quantidade_itens_do_carrinho(request, item_id):
    item = get_object_or_404(Carrinho, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('ver_carrinho')

def diminuir_quantidade_itens_do_carrinho(request, item_id):
    item = get_object_or_404(Carrinho, id=item_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('ver_carrinho')