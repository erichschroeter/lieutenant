# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import randomslugfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_entry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=randomslugfield.fields.RandomSlugField(default=0, editable=False, length=5, max_length=5, blank=True, unique=True),
            preserve_default=False,
        ),
    ]
