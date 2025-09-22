from django.db import models
import datetime
from django.utils import timezone

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