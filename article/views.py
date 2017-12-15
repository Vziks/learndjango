# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from querybuilder.query import Query

from .models import Article,Section
from pprint import pprint

# loader
def index(request):

    # section_list_ = Section.objects.all().order_by('section_title')

    query = Query().from_table(Section).order_by('section_title', desc=False)
    section_list = query.select()

    template = loader.get_template('article/index.html')
    context = {
        'section_list': section_list
    }
    return HttpResponse(template.render(context, request))

def section(request, section):
    try:
        section = Section.objects.get(section_url=section)
    except Section.DoesNotExist:
        raise Http404("Section does not exist")
    return render(request, 'article/section.html', {'section': section})

def detail(request, section, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'article/detail.html', {'article': article})