from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

