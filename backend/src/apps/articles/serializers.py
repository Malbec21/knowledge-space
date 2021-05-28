from django.db import transaction
from rest_framework import serializers

from src.apps.accounts.serializers import UserProfileSerializer
from src.apps.articles.models import Article, KeyWord


class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    authors_data = UserProfileSerializer(many=True, read_only=True)
    key_words = KeyWordSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {
            "authors": {"write_only": True},
            "bibliography_reference": {"required": True},
        }

    @transaction.atomic
    def create(self, validated_data):
        authors = validated_data.pop("authors")
        key_words = (
            validated_data.pop("key_words") if validated_data.get("key_words") else []
        )
        article = Article.objects.create(**validated_data)

        for author in authors:
            article.authors.add(author)

        if key_words:
            for kw in key_words:
                kw, _ = KeyWord.objects.get_or_create(name=kw["name"])
                article.key_words.add(kw)

        article.save()

        return article
