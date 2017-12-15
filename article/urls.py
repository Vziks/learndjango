# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'article'

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     # url(r'^latest\.html$', views.index),
#     url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
# ]


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<section>[\w]+)/$', views.section, name='section'),
    url(r'^(?P<section>[\w]+)/(?P<article_id>[0-9]+)/$', views.detail, name='article')
]