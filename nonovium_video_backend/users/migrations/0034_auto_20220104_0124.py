# Generated by Django 3.1.13 on 2022-01-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20220104_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.CharField(default='https://avatars.dicebear.com/api/avataaars/50019.svg?size=150', max_length=250, verbose_name='Profile Image URL'),
        ),
    ]
