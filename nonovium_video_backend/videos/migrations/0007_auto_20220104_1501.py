# Generated by Django 3.1.13 on 2022-01-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20220104_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='post_id',
            field=models.CharField(default='0be61e20-283d-418c-93da-09291ec2459c', editable=False, max_length=256),
        ),
    ]
