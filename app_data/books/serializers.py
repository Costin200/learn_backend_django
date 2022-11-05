from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=50)
    page_count = serializers.IntegerField()
    description = serializers.CharField(max_length=250, default="")

    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `AppUser` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.page_count = validated_data.get('page_count', instance.page_count)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
