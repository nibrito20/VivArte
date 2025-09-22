from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[" + str(self.id) + "]" + self.title 
    
    def detailedstr(self):
        return "[" + str(self.id) + "]" + self.title + "data: " + self.creationdate + "detalhes: " + self.details