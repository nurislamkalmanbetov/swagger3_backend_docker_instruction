from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "first_name",
            "phone",
            "category",
            "birthday",
            "position",
            "company",
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "first_name",
            "category",
            "phone",
            "birthday",
            "position",
            "company",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user


class FirstStepRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "first_name",
            "category",
        ]
        required = [
            "email",
            "first_name",
            "category",
        ]


class SecondStepRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "phone",
            "birthday",
            "position",
            "company",
        ]
        required = [
            "phone",
            "birthday",
            "position",
            "company",
        ]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False)


class LogoutSerializer(serializers.Serializer):
    access_token = serializers.CharField(
        required=True, allow_blank=False, allow_null=False
    )
    refresh_token = serializers.CharField(
        required=True, allow_blank=False, allow_null=False
    )
