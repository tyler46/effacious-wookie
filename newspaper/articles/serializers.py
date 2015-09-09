from rest_framework import serializers

from newspaper.articles.models import Article, Reporter


class ReporterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reporter


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article

