from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in list view
    list_filter = ('publication_year', 'author')            # Add filter sidebar by year and author
    search_fields = ('title', 'author')                     # Add search box for title and author

