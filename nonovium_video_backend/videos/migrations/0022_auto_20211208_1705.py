# Generated by Django 3.1.13 on 2021-12-08 17:05

import django.contrib.sites.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0004_alter_options_ordering_domain'),
        ('videos', '0021_auto_20211208_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='6e3dfead-b764-4f81-96d6-0d73dd6a289e', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='sites',
            field=models.ManyToManyField(default=django.contrib.sites.models.SiteManager.get_current, to='sites.Site'),
        ),
    ]
