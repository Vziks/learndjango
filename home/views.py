# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template('home/index.html')
    django_version = django.VERSION
    context = {'django_version': django_version}
    return HttpResponse(template.render(context, request))