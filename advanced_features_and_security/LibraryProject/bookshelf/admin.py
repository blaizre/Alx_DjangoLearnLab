from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Book, CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in list view
    list_filter = ('publication_year', 'author')            # Add filter sidebar by year and author
    search_fields = ('title', 'author')                     # Add search box for title and author

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "is_staff", "is_active", "role"]
    list_filter = ["is_staff", "is_active", "role"]
    fieldsets = UserAdmin.fieldsets + (
            (None, {"fields": ("role",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {"fields": ("role",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
