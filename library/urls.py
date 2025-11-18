from django.urls import path
from . import views  

app_name = 'library'

urlpatterns = [
    # --- MUDANÇA PRINCIPAL AQUI ---
    # 1. A Página Inicial (Raiz do site) agora chama a view 'index' (que carrega o home.html)
    path('', views.booklist, name='home'),

    # 2. A Lista de Livros agora fica em uma URL específica '/livros/'
    # Assim não mistura a capa do site com a lista completa.
    path('livros/', views.booklist, name="list"),

    # --- ROTAS QUE PERMANECEM IGUAIS ---
    path('adicionar-livro/', views.addbook, name="add"),
    path('lista-de-desejos/', views.wishlist_view, name="wishlist"),
    
    # Lógica da Wishlist
    path('lista-de-desejos/adicionar/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('lista-de-desejos/remover/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    # Filtros
    path('genero/<slug:genero_slug>/', views.booklist, name='lista_por_genero'),
    path('aval/<slug:rating_slug>', views.booklist, name='lista_por_avaliacao'),
    
    # Reviews e Detalhes
    path('submit_review/<int:book_id>/', views.submit_review, name='submit_review'),
    path('<slug:slug>', views.bookpage, name="detail"),
]