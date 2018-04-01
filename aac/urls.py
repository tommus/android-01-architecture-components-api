from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("aac.library.urls", "library"))),
]

admin.site.site_title = "AAC Sample API"
admin.site.site_header = "AAC Sample API"
