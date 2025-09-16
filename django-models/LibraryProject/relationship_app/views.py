from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book

# Create your views here.
#Function-based view.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


#Class-based view.
#List books
class ListDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/list_books.html'

#Library details of a specific library including books in that library.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

