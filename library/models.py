from django.db import models
import datetime
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    details = models.TextField(null=False)
    attempt = models.TextField()
    creationdate = models.DateTimeField("Criado em ")
    user = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #currency = models.CharField(max_length=3, choices=get_currencies) fazer depois opcao para mudar a moeda

    def __str__(self):
        return "[" + str(self.id) + "] " + self.title
    
    def recentlyputforoffer(self):
        return self.creationdate >= timezone.now() - datetime.timedelta(days=7)

    def detailedstring(self):
        return "id: " + str(self.id) + "; titulo: " + self.title + "; Preço: " + self.price + "; detalhes: " + self.details + "; tentativa: " + self.attempt + "; data criação: " + str(self.creationdate) + "; usuario: " + self.user


class Comments(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    votes = models.IntegerField(default=0)
    creationdate = models.DateTimeField("Criado em")
    user = models.CharField(max_length=200, null=False, default="anonimo")

    def __str__(self):
        return "[" + str(self.id) + "]" + self.text
    
    def recentlypublished(self):
        return self.creationdate >= timezone.now() - datetime.timedelta(days=3)
    
# Create your models here.

