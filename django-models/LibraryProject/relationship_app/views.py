from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()
    lines = [f"{book.title} by {book.author.name}" for book in books]
    response_text = "\n".join(lines) if lines else "No books available."
    return HttpResponse(response_text, content_type="text/plain")

