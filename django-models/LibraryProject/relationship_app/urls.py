from django.urls import path
from .views import list_books, register
from .views import LibraryDetailView, ListDetailView, LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name ='library-detail'),
    path('books/<int:pk>/', ListDetailView.as_view(), name = 'list-books'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name = 'logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian-view'),
    path('member/', views.member_view, name='member_view'),

]

