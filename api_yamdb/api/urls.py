from django.urls import include, path
from .views import get_jwt_token, register
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet,
                    GenreViewSet,
                    TitleViewSet)


v1_router = DefaultRouter()
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'genres', GenreViewSet)
v1_router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
