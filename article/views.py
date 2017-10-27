# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    return HttpResponse(latest_article_list)