from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from aac.library.views import (
    CoverViewSet,
    PublishingHouseViewSet,
    AuthorViewSet,
    BookViewSet
)

router = routers.DefaultRouter()
router.register(r'library/covers', CoverViewSet)
router.register(r'library/publishing_houses', PublishingHouseViewSet)
router.register(r'library/authors', AuthorViewSet)
router.register(r'library/books', BookViewSet)

urlpatterns = [
    url(r'', admin.site.urls),
    url(r'^api/', include(router.urls)),
]

admin.site.site_title = "AAC Sample API"
admin.site.site_header = "AAC Sample API"
