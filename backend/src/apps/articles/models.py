from django.db import models

from src.apps.accounts.models import User


class KeyWord(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Article(models.Model):
    class ArticleTypes(models.TextChoices):
        ARTICLE = "ARTICLE"
        THESIS = "THESIS"
        PATENT = "PATENT"

    title = models.CharField(max_length=256)
    summary = models.TextField()
    type = models.CharField(max_length=7, choices=ArticleTypes.choices)
    authors = models.ManyToManyField(User, related_name="articles")
    key_words = models.ManyToManyField(KeyWord, blank=True)
    scopus_indication = models.BooleanField(default=False)
    bibliography_reference = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
