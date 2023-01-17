from rest_framework import viewsets

from .permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer
from posts.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
