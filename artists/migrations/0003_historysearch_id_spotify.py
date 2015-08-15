# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20150813_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='historysearch',
            name='id_spotify',
            field=models.CharField(default=1212, max_length=100),
            preserve_default=False,
        ),
    ]
