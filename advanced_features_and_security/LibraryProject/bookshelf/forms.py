from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """Form for creating and editing books securely."""
    class Meta:
        model = Book
        fields = ["title", "author"]

class ExampleForm(forms.Form):
    """
    Example form to demonstrate CSRF protection and safe input handling.
    This can be used in a test template (form_example.html).
    """
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"}),
        required=False
    )

