# Generated by Django 3.1.14 on 2022-01-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_auto_20220123_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.CharField(default='https://avatars.dicebear.com/api/avataaars/82832.svg?size=150', max_length=250, verbose_name='Profile Image URL'),
        ),
    ]
