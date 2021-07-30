# Generated by Django 3.0.2 on 2021-07-26 12:16

import authentication.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0034_auto_20210721_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_picture',
            field=models.ImageField(blank=True, default=None, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/picture/', location='/opt/Ritesh_Office/SGSPL/Inkster/users/media/picture'), upload_to=authentication.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, default=None, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/picture/', location='/opt/Ritesh_Office/SGSPL/Inkster/users/media/picture'), upload_to=authentication.models.user_directory_path),
        ),
    ]
