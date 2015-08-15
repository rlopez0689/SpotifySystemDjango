# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_auto_20150531_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'avatars', blank=True),
        ),
    ]
