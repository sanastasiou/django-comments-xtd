# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments_xtd', '0003_auto_20170220_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xtdcomment',
            options={'ordering': ('submit_date',), 'permissions': [('can_moderate', 'Can moderate comments')], 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
    ]
