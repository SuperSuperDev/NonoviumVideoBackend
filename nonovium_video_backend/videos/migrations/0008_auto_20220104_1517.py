# Generated by Django 3.1.13 on 2022-01-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20220104_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='47de37c9-92f5-4d53-ac53-381f9f71c017', editable=False, max_length=256),
        ),
    ]
