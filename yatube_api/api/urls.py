from rest_framework.routers import DefaultRouter

from django.urls import path, include

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register(
    'api/v1/posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
]
