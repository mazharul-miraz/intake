# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0043_status_update_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusnotification',
            name='status_update',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='notification', to='intake.StatusUpdate'),
        ),
    ]
