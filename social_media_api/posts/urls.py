from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')

comments_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
comments_router.register(r'comments', CommonViewSet, basename='post-comments')

urlpatterns = router.urls + comments_router.urls


