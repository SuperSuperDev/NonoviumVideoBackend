# Generated by Django 3.1.13 on 2022-01-04 11:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0002_auto_20220104_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videofile',
            name='video_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
