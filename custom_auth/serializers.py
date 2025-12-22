from rest_framework import serializers
from custom_auth.models import User
from django.contrib.auth import authenticate, get_user_model

# User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:  # provides metadata for the serializer Class
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        # user = User.objects.create_user(
        #     email=validated_data['email'],
        #     password=validated_data['password']
        # )
        # return user
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user
