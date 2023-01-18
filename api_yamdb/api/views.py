from rest_framework import filters, viewsets

from .permissions import IsAdminOrReadOnly
from .serializers import GenreSerializer
from reviews.models import Genre


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
