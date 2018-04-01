from rest_framework import serializers

from aac.library import models


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cover
        fields = "__all__"


class PublishingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PublishingHouse
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"
