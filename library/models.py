from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class RatingSearch(models.Model):
    rating = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return str(self.rating)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.rating)
        super().save(*args, **kwargs)

class Book(models.Model):

    title = models.CharField(max_length=100)
    details = models.TextField()
    creationdate = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    banner = models.ImageField(default='fallack.png', blank=True)
    #stars = models.FloatField(,default=0) pra aparecer qual a media de estrelas do livro

    generos = models.ManyToManyField(Genre, blank=True)
    rating = models.ManyToManyField(RatingSearch, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.title 
    
    def detailedstr(self):
        return self.title + "data: " + str(self.creationdate) + "detalhes: " + self.details
    
class Comment(models.Model):
    pass

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'



class ReviewRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.book} : {self.rating}"

    def fullreview(self):
        return self.review
    
class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user.username} - {self.book.title} ({self.quantity})'
