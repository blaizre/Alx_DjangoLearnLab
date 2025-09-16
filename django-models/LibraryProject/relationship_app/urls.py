from django.urls import path
from . import views
from .views import LibraryDetailView, ListDetailView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name ='library-detail'),
    path('books/<int:pk>/', ListDetailView.as_view(), name = 'list-books'),
]

