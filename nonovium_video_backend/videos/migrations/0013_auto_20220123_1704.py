# Generated by Django 3.1.14 on 2022-01-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_auto_20220123_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='918417a6-a397-4bba-ae0d-35629e0bb7dd', editable=False, max_length=256),
        ),
    ]
