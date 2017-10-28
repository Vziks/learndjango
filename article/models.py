# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(null=True)
    summary = models.TextField(null=True)
    shortSummary = models.TextField(null=True)
    content = models.TextField(null=True)
    image = models.ImageField(
        'description of purpose',
        upload_to='%Y/%m/%d/',
        max_length=500,
        null=True,
        blank=True
    )
    summaryImage = models.ImageField(
        'description of purpose',
        upload_to='%Y/%m/%d/',
        max_length=500,
        null=True,
        blank=True
    )
    def __unicode__(self):
       return 'Article: ' + self.title

    def __str__(self):
        return 'Article: ' + self.title

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="/static/media/{}" width="150" height="150" />'.format(self.image) )

    image_tag.short_description = 'Image'

    def summary_image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="/static/media/{}" width="150" height="150" />'.format(self.summaryImage) )

    summary_image_tag.short_description = 'ImageSum'