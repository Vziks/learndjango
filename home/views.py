# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def error_404(request):
    template = loader.get_template('error_404.html')
    context = Context({
        'message': 'All: %s' % request,
    })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)


def error_500(request):
    template = loader.get_template('error_500.html')
    context = Context({
        'message': 'All: %s' % request,
    })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=500)