from django.urls import path
from .views import list_books
from .views import LibraryDetailView, ListDetailView, RegisterView, CustomLoginView, CustomLogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name ='library-detail'),
    path('books/<int:pk>/', ListDetailView.as_view(), name = 'list-books'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', CustomLogoutView.as_view(), name = 'logout'),
]

