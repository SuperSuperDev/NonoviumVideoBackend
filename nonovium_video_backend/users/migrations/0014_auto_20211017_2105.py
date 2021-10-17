# Generated by Django 3.1.13 on 2021-10-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_auto_20211017_1824"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_image",
            field=models.CharField(
                default="https://avatars.dicebear.com/api/avataaars/28422.svg?size=150",
                max_length=250,
                verbose_name="Profile Image URL",
            ),
        ),
    ]
