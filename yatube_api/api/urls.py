from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register('v1/groups', GroupViewSet)
router_v1.register(
    'v1/posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
