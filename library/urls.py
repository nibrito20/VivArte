from django.urls import path
from . import views  

app_name = 'library'

urlpatterns = [
    path('', views.booklist, name='home'),

    path('livros/', views.booklist, name="list"),

    path('adicionar-livro/', views.addbook, name="add"),

    path('lista-de-desejos/', views.wishlist_view, name="wishlist"),
    path('lista-de-desejos/adicionar/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('lista-de-desejos/remover/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    path('genero/<slug:genero_slug>/', views.booklist, name='lista_por_genero'),
    path('aval/<slug:rating_slug>', views.booklist, name='lista_por_avaliacao'),
    
    path('submit_review/<int:book_id>/', views.submit_review, name='submit_review'),
    path('<slug:slug>', views.bookpage, name="detail"),

    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:book_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:item_id>/', views.remover_item_do_carrinho, name='remover_item'),
    path('carrinho/aumentar/<int:item_id>/', views.aumentar_quantidade_itens_do_carrinho, name='aumentar_quantidade'),
    path('carrinho/diminuir/<int:item_id>/', views.diminuir_quantidade_itens_do_carrinho, name='diminuir_quantidade'),
]