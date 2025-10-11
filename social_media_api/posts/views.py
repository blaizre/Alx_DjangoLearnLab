from django.shortcuts import render
from rest_framework import viewsets, pagination, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializers, CommentSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    #Automatically provides list, create, retrieve, update, and destroy actions for posts
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    #Automatically provides CRUD options for comments.

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedReadOnly, IsOwnerOrReadONly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        #Filters comments by th post they are related to from the URL.
        return Comment.objects.fileter(post_id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        #Automatically associate the comment with post from the URL and author with current user.
        serializer.save(
                author=self.request.user,
                post_id=self.kwargs['post_pk']
        )

