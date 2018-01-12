from rest_framework.serializers import ModelSerializer

from aac.library.models import (
    Cover,
    PublishingHouse,
    Author,
    Book
)


class CoverSerializer(ModelSerializer):
    class Meta:
        model = Cover
        fields = '__all__'


class PublishingHouseSerializer(ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
