from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
# importar usuarios from users.migrations


def booklist(request):
    books = Book.objects.all().order_by('-creationdate')
    return render(request, 'library/booklist.html', { 'books': books})

def bookpage(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'library/bookpage.html', { 'book': book})


@login_required(login_url="/users/login/")
def wishlist(request):

   return render(request, 'library/wishlist.html')

#wishes = user.objecs.wished().order_by('-creationdate') isso seria a base para a lista de desejos
#wishes = 
#return render(request, 'library/wishlist.html', { 'wishes' : wishes})
@login_required(login_url="/users/login/")
def addbook(request):
    
    return render(request, 'library/addbook.html')

#add = 
#return render(request, 'library/addbook.html', { 'add' : add})