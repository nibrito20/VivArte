from django.contrib import admin
from django.utils.html import format_html
from .models import Book, Genre, ReviewRating, RatingSearch

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações Principais', {
            'fields': ['title', 'author', 'details', 'slug', 'banner', 'price']
        }),
        ('Categorização e Avaliação', {
            'fields': ['generos', 'rating']
        }),
    ]
    filter_horizontal = ('generos','rating')

    list_display = ('title', 'cover_preview', 'slug')
    
    def cover_preview(self, obj):
        if obj.banner:
            return format_html('<img src="{}" style="width: 60px; height:auto;" />', obj.banner.url)
        return "-"
    cover_preview.short_description = 'Capa'

admin.site.register(Genre) 
admin.site.register(Book, BookAdmin) 
admin.site.register(ReviewRating)
admin.site.register(RatingSearch)
