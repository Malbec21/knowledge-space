from django.db.models import QuerySet
from django_filters import rest_framework as filters

from src.apps.accounts.models import User
from src.apps.articles.models import Article


class ArticleListFilterSet(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    summary = filters.CharFilter(lookup_expr="icontains")
    key_words__name = filters.CharFilter(lookup_expr="icontains")
    author = filters.ModelChoiceFilter(
        field_name="author",
        label="Author",
        queryset=User.objects.all(),
        method="filter_author",
    )

    class Meta:
        model = Article
        fields = (
            "title",
            "summary",
        )

    @staticmethod
    def filter_author(queryset, name, value) -> QuerySet[Article]:
        return queryset.filter(authors__id=value.id)
