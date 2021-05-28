import base64
import re
from binascii import Error

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from src.apps.accounts.models import User, WorkPlace


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class UploadFileSerializer(serializers.Serializer):
    filename = serializers.CharField()
    file = serializers.CharField()

    def validate(self, attrs):
        try:
            attrs = ContentFile(
                base64.b64decode(re.search(r"base64,(.*)", attrs["file"]).group(1)),
                f"{attrs['filename']}",
            )
        except Error:
            raise serializers.ValidationError("Invalid base64-string input")
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    avatar = UploadFileSerializer(write_only=True, required=False)
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "avatar",
            "avatar_url",
            "email",
            "first_name",
            "last_name",
            "patronymic_name",
            "place_of_work",
            "position",
            "academic_status",
            "scientific_degree",
        )
        extra_kwargs = {
            "email": {"read_only": True},
            "place_of_work": {"required": False},
        }

    def get_avatar_url(self, user: User):
        try:
            return user.avatar.url
        except ValueError:
            return

    def update(self, instance, validated_data):
        if (
            validated_data.get("avatar")
            and instance.avatar.name != "default_avatar.png"
        ):
            instance.avatar.delete()
        return super(UserProfileSerializer, self).update(instance, validated_data)


class WorkPlaceSerializer(serializers.ModelSerializer):
    employees = UserProfileSerializer(many=True)

    class Meta:
        model = WorkPlace
        fields = "__all__"


class ExpandedTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["patronymic_name"] = user.patronymic_name

        return token
