# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160921_0006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u4ea7\u54c1\u5206\u7c7b', 'verbose_name_plural': '\u4ea7\u54c1\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'verbose_name': '\u5173\u952e\u8bcd', 'verbose_name_plural': '\u5173\u952e\u8bcd'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '\u4ea7\u54c1', 'verbose_name_plural': '\u4ea7\u54c1'},
        ),
    ]
