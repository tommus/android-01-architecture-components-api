from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from aac.library.models import (
    Cover,
    PublishingHouse,
    Author,
    Book
)
from aac.library.serializers import (
    CoverSerializer,
    PublishingHouseSerializer,
    AuthorSerializer,
    BookSerializer
)


class CoverViewSet(
    CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin,
    UpdateModelMixin, GenericViewSet):
    filter_fields = ["active"]
    permission_classes = [AllowAny]
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer


class PublishingHouseViewSet(
    CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin,
    UpdateModelMixin, GenericViewSet):
    filter_fields = ["active"]
    permission_classes = [AllowAny]
    queryset = PublishingHouse.objects.all()
    serializer_class = PublishingHouseSerializer


class AuthorViewSet(
    CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin,
    UpdateModelMixin, GenericViewSet):
    filter_fields = ["active"]
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(
    CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin,
    UpdateModelMixin, GenericViewSet):
    filter_fields = ["cover", "author", "publishing_house", "active"]
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
