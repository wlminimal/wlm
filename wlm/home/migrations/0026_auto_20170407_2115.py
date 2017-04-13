# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0025_auto_20170407_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='hero_image',
            field=models.ForeignKey(help_text='1680 x 1100 image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='main_subtitle',
            field=models.TextField(default='Get in touch with us and we will help you with your next project.', help_text='Main subtitle, 100 Max Length', max_length=100),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='main_title_1',
            field=models.CharField(default='We would love', help_text='Main title, 40 Max Characters', max_length=40),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='main_title_2',
            field=models.CharField(default='to hear from you', help_text='Main title, 40 Max Characters', max_length=40),
        ),
    ]
