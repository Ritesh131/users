# Generated by Django 3.0.2 on 2020-12-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_auto_20201203_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='from_request',
            field=models.IntegerField(blank=True, default=None, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='to_request',
            field=models.IntegerField(blank=True, default=None, max_length=5000, null=True),
        ),
    ]
