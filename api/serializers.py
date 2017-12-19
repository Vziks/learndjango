from rest_framework import serializers
from article import models as ArticleModels

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModels.Article
        exclude = ()

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModels.Section
        exclude = ()