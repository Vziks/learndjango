# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-19 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20171212_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'article', 'verbose_name_plural': 'articles'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'section', 'verbose_name_plural': 'sections'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='shortSummary',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='%Y/%m/%d/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='pudDate'),
        ),
        migrations.AlterField(
            model_name='article',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section', to='article.Section', verbose_name='section'),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(null=True, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='article',
            name='summaryImage',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='%Y/%m/%d/', verbose_name='summaryImage'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_title',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_url',
            field=models.CharField(max_length=50, verbose_name='url'),
        ),
    ]
