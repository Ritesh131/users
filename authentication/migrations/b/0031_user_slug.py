# Generated by Django 3.0.2 on 2021-01-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0030_user_profile_privacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=500),
        ),
    ]
