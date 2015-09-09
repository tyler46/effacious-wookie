from rest_framework import viewsets

from newspaper.articles.models import Article, Reporter
from newspaper.articles.serializers import (ArticleSerializer,
                                            ReporterSerializer)


class ReporterViewSet(viewsets.ModelViewSet):
    """A view for viewing only reporter instances."""
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing article instances."""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

