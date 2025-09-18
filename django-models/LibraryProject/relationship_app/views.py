from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
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

#Login.
class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

#Logout.
class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

#Register FBV.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})

