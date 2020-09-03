from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from users.models import BaseUser


class CustomLoginSerializer(LoginSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    username = None

    def get_cleaned_data(self):
        super().get_cleaned_data()

        return {
            "email": self.validated_data.get("email", ""),
            "password": self.validated_data.get("password", ""),
        }


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    username = None

    def get_cleaned_data(self):
        super().get_cleaned_data()

        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ("id", "email", "first_name", "last_name")
        read_only_fields = ("email",)
