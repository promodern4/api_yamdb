from rest_framework import viewsets

from .permissions import IsAdminOrReadOnly
from .serializers import TitleSerializer
from posts.models import Title


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
