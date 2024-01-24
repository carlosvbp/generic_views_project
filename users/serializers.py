from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # artistic_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    full_name = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "full_name", "artistic_name"]

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()

        return instance
