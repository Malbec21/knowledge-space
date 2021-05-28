from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from src.apps.accounts.mixins import PermissionPerActionMixin
from src.apps.articles.filters import ArticleListFilterSet
from src.apps.articles.models import Article
from src.apps.articles.permissions import IsAuthor
from src.apps.articles.serializers import ArticleSerializer


class ArticleViewSet(PermissionPerActionMixin, viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ArticleListFilterSet
    permission_classes_by_action = {
        "create": (IsAuthenticated,),
        "update": (IsAuthor,),
        "partial_update": (IsAuthor,),
        "destroy": (IsAuthor,),
    }
