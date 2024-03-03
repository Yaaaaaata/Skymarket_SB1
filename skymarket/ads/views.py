from rest_framework import pagination, viewsets
from .models import Ad, Comment
from .serializers import AdSerializer, CommentSerializer, AdDetailSerializer
from .permissions import IsAuthorOrReadOnly


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = AdPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AdDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

