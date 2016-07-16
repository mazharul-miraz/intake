# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0013_add_county_model'),
        ('user_accounts', '0005_organization_is_receiving_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizations', to='intake.County'),
        ),
    ]
