from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvFilter
from advertisements.permissions import IsCreatorOrReadOnly
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters import rest_framework as filters





class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = [IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly | IsAdminUser]
    filterset_class = AdvFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    # обошелся обычным способом, указанным в туторьялах,
    # а этот не очень понял; как реализовать что-то похожее на has_object_permission()

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update", "delete"]:
    #         if self.request.user ==
    #
    #         return [IsAuthenticatedOrReadOnly()]
    #     return []

