# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from article import models as ArticleModels
from .serializers import ArticleSerializer, SectionSerializer

# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

# @api_view(["GET"])
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticleModels.Article.objects.all()
    serializer_class = ArticleSerializer

class DetailsArticleView(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = ArticleModels.Article.objects.all()
    serializer_class = ArticleSerializer

class SelectionViewSet(viewsets.ModelViewSet):
    queryset = ArticleModels.Section.objects.all()
    serializer_class = SectionSerializer

class DetailsSectionView(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = ArticleModels.Section.objects.all()
    serializer_class = SectionSerializer