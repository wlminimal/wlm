# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20170405_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='first_quote',
            field=wagtail.wagtailcore.fields.RichTextField(default="when you don't create things, you become defined by your tastes rather than ability. your tastes only narrow & exclude people. so create."),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='first_quote_speaker',
            field=models.CharField(default='Why The Lucky Stiff', help_text='30 Max Characters', max_length=30),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='second_quote',
            field=wagtail.wagtailcore.fields.RichTextField(default='In any moment of decision, the best thing you can do is the right thing, the next best thing is the wrong thing, and the worst thing you can do is nothing.'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='second_quote_speaker',
            field=models.CharField(default='Theodore Roosevelt', help_text='30 Max Characters', max_length=30),
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='main_title1_em',
            field=models.CharField(default='things', help_text='Emphasize Text, 30 Max Chracters', max_length=30),
        ),
    ]
