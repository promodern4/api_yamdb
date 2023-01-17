from rest_framework import viewsets

from .permissions import IsAdminOrReadOnly
from .serializers import GenreSerializer
from posts.models import Genre


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
