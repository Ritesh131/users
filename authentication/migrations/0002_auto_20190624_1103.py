# Generated by Django 2.2.2 on 2019-06-24 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=3)),
                ('phone_code', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='local_area',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_code',
            field=models.CharField(default=91, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='terms_and_conditions',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.Country'),
        ),
    ]
