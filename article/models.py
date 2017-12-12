# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Section(models.Model):
    class Meta:
        db_table = 'section'
    section_title = models.CharField(max_length=200)
    section_url = models.CharField(max_length=50)
    section_description = models.TextField()

    def __str__(self):
        return self.section_title

class Article(models.Model):
    class Meta:
        db_table = 'article'
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(null=True)
    summary = models.TextField(null=True)
    shortSummary = models.TextField(null=True)
    content = models.TextField(null=True)
    section = models.ForeignKey(Section, null=True, blank=True)
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
        return mark_safe('<img src="/uploads/media/{}" width="150" height="150" />'.format(self.image) )

    image_tag.short_description = 'Image'

    def summary_image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="/uploads/media/{}" width="150" height="150" />'.format(self.summaryImage) )

    summary_image_tag.short_description = 'ImageSum'