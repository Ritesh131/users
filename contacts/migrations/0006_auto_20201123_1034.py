# Generated by Django 3.0.2 on 2020-11-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contact_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
