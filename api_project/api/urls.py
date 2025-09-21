from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

#Create router and register the ViewSet
router = DefaultRouter()
router.register(r'book_all', BookViewSet, basename='book-all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
