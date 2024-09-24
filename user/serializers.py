from rest_framework import serializers

from user.models import Users


class UserSerializer(serializers.ModelSerializer):
    """User model serializer."""
    class Meta:
        model = Users
        fields = ("email", "password",)


class UserListSerializer(serializers.ModelSerializer):
    """User list serializer."""
    class Meta:
        model = Users
        fields = ("email",)
