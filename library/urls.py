from django.urls import path
from . import views  

app_name = 'library'

urlpatterns = [

    path('adicionar-livro/', views.addbook, name="add"),
    path('lista-de-desejos/', views.wishlist_view, name="wishlist"),
    
    path('lista-de-desejos/adicionar/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('lista-de-desejos/remover/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('genero/<slug:genero_slug>/', views.booklist, name='lista_por_genero'),
    path('submit_review/<int:book_id>/', views.submit_review, name='submit_review'),
    path('', views.booklist, name="list"),

    path('<slug:slug>', views.bookpage, name="detail"),
    
]