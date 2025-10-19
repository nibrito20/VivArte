from django.contrib import admin
from .models import Book, Genre
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações Principais', {
            'fields': ['title', 'details', 'slug', 'banner']
        }),
        ('Categorização e Avaliação', {
            'fields': ['generos', 'aval']
        }),
    ]
    filter_horizontal = ('generos',)
# Register your models here.
admin.site.register(Genre) 
admin.site.register(Book, BookAdmin) 
