# Generated by Django 3.0.2 on 2021-07-27 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art_group', '0009_grouppost_description'),
        ('art_app', '0013_auto_20210727_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='userart',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='art_group.Group'),
        ),
    ]
