# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='group',
            new_name='usergroup',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('username', 'usergroup')]),
        ),
    ]
