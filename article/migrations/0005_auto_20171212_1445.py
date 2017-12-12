# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20171028_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=200)),
                ('section_url', models.CharField(max_length=50)),
                ('section_description', models.TextField()),
            ],
            options={
                'db_table': 'section',
            },
        ),
        migrations.AlterModelTable(
            name='article',
            table='article',
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Section'),
        ),
    ]
