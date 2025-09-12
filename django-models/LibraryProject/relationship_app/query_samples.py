#!/bin/bash/python3

from relationship_app models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Books.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []
#List all books in a library.
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=Library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

#Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (lLibrary.DoesNotExist, Librarian.DoesNotExist):
        return None
