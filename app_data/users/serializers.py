from rest_framework import serializers

from users.models import AppUser


class AppUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    age = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `AppUser` instance, given the validated data.
        """
        return AppUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `AppUser` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
