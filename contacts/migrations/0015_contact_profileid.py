# Generated by Django 3.0.2 on 2020-12-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_group_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profileId',
            field=models.IntegerField(default=None, max_length=5000),
        ),
    ]
