from django.urls import path
from .views import list_books
from .views import LibraryDetailView, ListDetailView, RegisterView, LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name ='library-detail'),
    path('books/<int:pk>/', ListDetailView.as_view(), name = 'list-books'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name = 'logout'),
]

