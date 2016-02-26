# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='video_data',
            field=jsonfield.fields.JSONField(help_text='For advanced users only \u2014 please do not edit this data unless you know what you are doing.', verbose_name='YouTube Data'),
            preserve_default=True,
        ),
    ]
