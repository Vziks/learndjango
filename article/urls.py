from django.conf.urls import url

from . import views

app_name = 'article'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^latest\.html$', views.index),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]