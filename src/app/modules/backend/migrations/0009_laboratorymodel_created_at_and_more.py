# Generated by Django 5.2.1 on 2025-05-17 16:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_providermodel_lotmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
