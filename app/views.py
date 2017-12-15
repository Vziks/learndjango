# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def handler404(request):
    return render(request, 'error_404.html', status=404)

def handler500(request):
    return render(request, 'error_500.html', status=500)