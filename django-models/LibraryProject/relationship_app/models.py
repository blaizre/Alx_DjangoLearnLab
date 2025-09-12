from django.db import models

# Create your models here.

class Author(models.Models):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Models):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Library(models.Models):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Models):
    name = models.CharField(max_length=100)
    library = models.oneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


