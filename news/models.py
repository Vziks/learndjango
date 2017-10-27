# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(null=True)
    summaryImage = models.FileField(upload_to='uploads/%Y/%m/%d/')
    image = models.FileField(upload_to='uploads/%Y/%m/%d/')
    shortSummary = models.TextField(null=True)
    content = models.TextField(null=True)