from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.articles.views import ArticleViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet, basename="articles")

urlpatterns = [
    path("", include(router.urls)),
]
