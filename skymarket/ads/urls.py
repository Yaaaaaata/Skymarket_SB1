from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AdViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
