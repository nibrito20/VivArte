from django.urls import path
from . import views  

app_name = 'library'

urlpatterns = [
    path('', views.booklist, name="list"),
    path('lista-de-desejos', views.wishlist, name="wish"),
    path('adicionar-livro', views.addbook, name="add"),

    path('<slug:slug>', views.bookpage, name="page"),
    
]