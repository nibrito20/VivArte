from django.contrib import admin
from .models import Book, Genre, ReviewRating
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações Principais', {
            'fields': ['title', 'details', 'slug', 'banner']
        }),
        ('Categorização e Avaliação', {
            'fields': ['generos']
        }),
    ]
    filter_horizontal = ('generos',)
# Register your models here.
admin.site.register(Genre) 
admin.site.register(Book, BookAdmin) 
admin.site.register(ReviewRating)
