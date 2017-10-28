# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    # fields = ( 'image_tag','title','description','image','externalURL', )
    readonly_fields = ('image_tag','summary_image_tag')

admin.site.register(Article, ArticleAdmin)