from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.

#Only users with 'can_view' permission can see this view.
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {"books": books})

#Only users with 'can_create' permission can add books.
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title,  author=author)
        return redirect("list_books")
    return render(request, "bookshelf/add_book.html")

#Only users with 'can_edit' permission can edit books.
@permisssion_required("bookshelf.can_edit", raise_excpetion=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("list_books")
    return render(request, "bookshelf/edit_book.html", {"book": book})

#Only users with 'can_delete' permisssion can delete books.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(requset, "bookshelf/delete_book.html", {"book": book})

