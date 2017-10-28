# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Article

# loader
def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]

    template = loader.get_template('article/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))


    # return HttpResponse(template.render({
    # return HttpResponse(template.render({
    #     'latest_article_list': latest_article_list,
    # }, request))

# Render
# def index(request):
#     latest_article_list = Article.objects.order_by('-pub_date')[:5]
#     context = {'latest_article_list': latest_article_list}
#     return render(request, 'article/index.html', context)

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'article/detail.html', {'article': article})

#short
# def detail(request, article_id):
#     article = get_object_or_404(Article, pk=article_id)
#     return render(request, 'polls/detail.html', {'article': article})