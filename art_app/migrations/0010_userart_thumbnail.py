# Generated by Django 3.0.2 on 2021-05-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_app', '0009_userart_media_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userart',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='directory_path'),
        ),
    ]
