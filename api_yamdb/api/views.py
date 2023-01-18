from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAdminOrReadOnly
from .serializers import TitleSerializer, TitleListSerializer
from reviews.models import Title


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category__slug', 'genre__slug', 'name', 'year')

    def get_serializer_class(self):
        # Для чтения списка или одного эксземпляра
        if self.action in ('list', 'retrieve'):
            return TitleListSerializer
        return TitleSerializer
