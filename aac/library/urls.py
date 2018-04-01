from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from aac.library.views import (
    CoverViewSet,
    PublishingHouseViewSet,
    AuthorViewSet,
    BookViewSet
)

router = routers.DefaultRouter()
router.register("covers", CoverViewSet)
router.register("publishing_houses", PublishingHouseViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [
    path("library/", include(router.urls))
]
