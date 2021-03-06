# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20170410_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='contact_title',
            field=models.TextField(default='Interested in working with us?', help_text='100 Max Characters', max_length=200),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='contact_title_alt',
            field=models.TextField(default='We enjoy meeting new people', help_text='100 Max Characters', max_length=200),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='contact_title',
            field=models.TextField(default='Interested in working with us?', help_text='100 Max Characters', max_length=200),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='contact_title_alt',
            field=models.TextField(default='We enjoy meeting new people', help_text='100 Max Characters', max_length=200),
        ),
    ]
