# Generated by Django 3.0.2 on 2020-11-20 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_auto_20200624_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
