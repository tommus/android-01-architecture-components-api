from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    Model,
    TextField,
    CASCADE
)

from django.utils.translation import ugettext_lazy as _


class Cover(Model):
    name = CharField(max_length=127, verbose_name=_('Name'))
    active = BooleanField(default=True, verbose_name=_('Active'))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Cover')
        verbose_name_plural = _('Covers')


class PublishingHouse(Model):
    name = CharField(max_length=255, verbose_name=_('Name'))
    active = BooleanField(default=True, verbose_name=_('Active'))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Publishing House')
        verbose_name_plural = _('Publishing Houses')


class Author(Model):
    first_name = CharField(max_length=127, verbose_name=_('First name'))
    last_name = CharField(max_length=127, verbose_name=_('Last name'))
    active = BooleanField(default=True, verbose_name=_('Active'))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return str('{} {}'.format(self.first_name, self.last_name))

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Book(Model):
    title = CharField(max_length=255, verbose_name=_('Title'))
    pages = IntegerField(default=1, verbose_name=_('Pages'))
    description = TextField(max_length=1024, verbose_name=_('Description'))
    isbn = CharField(max_length=127, verbose_name=_('ISBN'))
    quantity = IntegerField(default=1, verbose_name=_('Quantity'))
    cover = ForeignKey(Cover, verbose_name=_('Cover'), on_delete=CASCADE)
    author = ForeignKey(Author, verbose_name=_('Author'), on_delete=CASCADE)
    publishing_house = ForeignKey(PublishingHouse, verbose_name=_('Publishing house'), on_delete=CASCADE)
    active = BooleanField(default=True, verbose_name=_('Active'))
    created_at = DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return str('{} - {}'.format(self.title, self.author.__str__()))

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
