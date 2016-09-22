# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-20 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0012_organization_show_pdf_only'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('text', models.TextField()),
                ('walk_in_hours', models.TextField(blank=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='user_accounts.Organization')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]