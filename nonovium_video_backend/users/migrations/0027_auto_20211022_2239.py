# Generated by Django 3.1.13 on 2021-10-22 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0026_auto_20211021_0241"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_image",
            field=models.CharField(
                default="https://avatars.dicebear.com/api/avataaars/12918.svg?size=150",
                max_length=250,
                verbose_name="Profile Image URL",
            ),
        ),
    ]
