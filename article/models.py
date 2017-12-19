# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Section(models.Model):
    class Meta:
        db_table = 'section'
        verbose_name = _('section')
        verbose_name_plural = _('sections')
    section_title = models.CharField(max_length=200, verbose_name = _('name'))
    section_url = models.CharField(max_length=50, verbose_name = _('url'))
    section_description = models.TextField(verbose_name = _('description'))

    def __str__(self):
        return self.section_title

    def __unicode__(self):
        return '%s' % (self.section_title)

class Article(models.Model):
    class Meta:
        db_table = 'article'
        verbose_name = _('article')
        verbose_name_plural = _('articles')
    title = models.CharField(max_length=255, verbose_name = _('title'))
    pub_date = models.DateTimeField(null=True, verbose_name = _('pudDate'))
    summary = models.TextField(null=True, verbose_name = _('summary'))
    content = models.TextField(null=True, verbose_name = _('content'))
    section = models.ForeignKey(Section, related_name='section', on_delete=models.CASCADE, null=True, blank=True, verbose_name = _('section'))
    image = models.ImageField(
        _('image'),
        upload_to='%Y/%m/%d/',
        max_length=500,
        null=True,
        blank=True
    )
    summaryImage = models.ImageField(
        _('summaryImage'),
        upload_to='%Y/%m/%d/',
        max_length=500,
        null=True,
        blank=True,

    )

    def __unicode__(self):
       return self.title

    def __str__(self):
        return self.title

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="/uploads/media/{}" width="150" height="150" />'.format(self.image) )

    image_tag.short_description = 'Image'

    def summary_image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="/uploads/media/{}" width="150" height="150" />'.format(self.summaryImage) )

    summary_image_tag.short_description = 'ImageSum'