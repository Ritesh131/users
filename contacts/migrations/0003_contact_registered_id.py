# Generated by Django 2.2.6 on 2019-11-07 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20191101_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='registered_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
