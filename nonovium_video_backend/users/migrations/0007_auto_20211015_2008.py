# Generated by Django 3.1.13 on 2021-10-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20211015_2007"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_image",
            field=models.CharField(
                default="https://avatars.dicebear.com/api/avataaars/69128.svg?size=150",
                max_length=250,
            ),
        ),
    ]
