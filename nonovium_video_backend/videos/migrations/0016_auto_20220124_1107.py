# Generated by Django 3.1.14 on 2022-01-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0015_auto_20220123_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='888114d6-ca78-467b-9681-03a1591310fe', editable=False, max_length=256),
        ),
    ]
