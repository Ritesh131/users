# Generated by Django 3.0.2 on 2021-03-14 11:59

import authentication.models
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('authentication', '0032_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=35, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('slug', models.SlugField(default='', editable=False, max_length=500)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone_code', models.CharField(blank=True, max_length=3, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=1, null=True)),
                ('location', models.TextField(default='', null=True)),
                ('connection_status', models.CharField(choices=[('O', 'Online'), ('F', 'Offline')], default='F', max_length=1)),
                ('connection_sent', models.IntegerField(default=0)),
                ('connection_received', models.IntegerField(default=0)),
                ('deal_requested', models.IntegerField(default=0)),
                ('deal_accepted', models.IntegerField(default=0)),
                ('deal_proposed', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, default=None, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/picture/', location='/opt/apps/media/picture'), upload_to=authentication.models.user_directory_path)),
                ('cover_picture', models.ImageField(blank=True, default=None, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/picture/', location='/opt/apps/media/picture'), upload_to=authentication.models.user_directory_path)),
                ('pin_enabled', models.BooleanField(default=False)),
                ('post_code', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('house', models.CharField(default='', max_length=100)),
                ('date_of_birth', models.CharField(default='', max_length=50)),
                ('profile_privacy', models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE')], default='PUBLIC', max_length=20)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.Country')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
    ]
