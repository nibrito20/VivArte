from django.urls import path
from . import views  

app_name = 'library'

urlpatterns = [
    path('', views.booklist, name="list"),
    path('<slug:slug>', views.bookpage, name="page"),
]