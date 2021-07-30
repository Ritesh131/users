# Generated by Django 3.0.2 on 2021-07-16 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stream_app', '0002_auto_20210623_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='stream_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stream',
            name='type',
            field=models.CharField(choices=[('free', 'free'), ('premium', 'premium')], default='free', max_length=15),
        ),
        migrations.CreateModel(
            name='StreamSubcribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream_app.Stream')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
