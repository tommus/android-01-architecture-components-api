from django.contrib.admin import (
    ModelAdmin,
    register
)

from aac.library.models import (
    Cover,
    PublishingHouse,
    Author,
    Book
)


@register(Cover)
class CoverAdmin(ModelAdmin):
    list_display = ['name', 'active']
    list_editable = ['active']
    list_filter = ['active']


@register(PublishingHouse)
class PublishingHouseAdmin(ModelAdmin):
    list_display = ['name', 'active']
    list_editable = ['active']
    list_filter = ['active']


@register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ['__str__', 'active']
    list_editable = ['active']
    list_filter = ['active']


@register(Book)
class BookAdmin(ModelAdmin):
    list_display = ['title', 'active']
    list_editable = ['active']
    list_filter = ['cover', 'author', 'publishing_house', 'active']
