# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ArticleConfig(AppConfig):
    name = 'article'
    verbose_name = _('articles')
