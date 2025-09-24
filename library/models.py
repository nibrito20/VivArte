from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    creationdate = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    banner = models.ImageField(default='fallack.png', blank=True)

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
