# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20170405_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='fifth_description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Description for what we do'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='first_description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Description for what we do'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='fourth_description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Description for what we do'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='main_subtitle',
            field=wagtail.wagtailcore.fields.RichTextField(default='Main Subtitle'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='main_title1',
            field=models.CharField(default='These are the ', help_text='Main Title, 20 Max Characters', max_length=20),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='main_title1_em',
            field=models.CharField(default='thiings', help_text='Emphasize Text, 30 Max Chracters', max_length=30),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='main_title2',
            field=models.CharField(default='we are ', help_text='Second line title, 20 Max Characters', max_length=20),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='main_title2_em',
            field=models.CharField(default='good at.', help_text='Emphasize Text, 30 Max Characters', max_length=30),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='second_description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Description for what we do'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='sixth_description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Description for what we do'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='third_description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Description for what we do'),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='what_we_do_fifth',
            field=models.CharField(default='Ongoing Support', help_text='20 Max Characters', max_length=20),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='what_we_do_first',
            field=models.CharField(default='Make Websites', help_text='20 Max Characters', max_length=20),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='what_we_do_fourth',
            field=models.CharField(default='E-Commerce Consulting', help_text='30 Max Characters', max_length=30),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='what_we_do_second',
            field=models.CharField(default='Photography', help_text='20 Max Characters', max_length=20),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='what_we_do_sixth',
            field=models.CharField(default='Make Websites', help_text='20 Max Characters', max_length=20),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='what_we_do_third',
            field=models.CharField(default='Build E-Commerce', help_text='20 Max Characters', max_length=20),
        ),
    ]
