from rest_framework import serializers
from .models import Article, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article