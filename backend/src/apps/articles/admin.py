from django.contrib import admin

from src.apps.articles.models import Article, KeyWord

admin.site.register(Article)
admin.site.register(KeyWord)
