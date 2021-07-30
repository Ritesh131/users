"""
Django settings for users project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import mimetypes
from pathlib import Path
mimetypes.add_type("text/css", ".css", True)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '../'))
DB_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '81&q$+o#^wgs7e9b_g*a^f)zw3npz(kq!ei!8wfg)*=x-q^^8v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'channels',
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'authentication',
    'rback',
    'token_storage',
    'contacts',
    'drf_yasg',
    'django_rest_passwordreset',
    'art_app.apps.ArtAppConfig',
    'art_group',
    'messanger',
    'payment_app',
    'stream_app',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'users.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# SANDBOX_ACCOUNT = 'sb-wxpkh6411895@business.example.com'
# CLIENT_ID = 'AQ8hsdUQ2GkGlzEL1WtBm6nyPdeijH3mC7nBPxbiz1OscEnjczlSxBtL0VDdXnRqrX_67iD7feA42zsp'

STRIPE_PUBLISH_KEY = 'pk_test_IUQKmcTUVMIdHsty0GNNm9Ap00TfDBP4L8'
STRIPE_SECRET_KEY = 'sk_test_6GJHD7Ofhck6CY1lyk6V99nP00mpx6JJXg'


PAYPAL_CLIENT_ID = "AR-MM1kWRLySjhiT1OgIDnV81nmQ7a82y-uzu9Z8hgP7DC6_252Ve2_MFplMSlpFgKk80TSO0eqklmXk"
PAYPAL_SECRET_ID = "EA_3uOcMr9VUSIjy_VOTW3onYUGs7RRKiuHjNnM6Y36zCOd1mqo6a7hNJ8VU0YHEycafj1St05Y35Ih2"

VIMEO_ACCESS_TOKEN = "095ae62bf081ea4d74feb3da3f3b75fc"
VIMEO_CLIENT_ID = "f06eea4ff16caae089d8999e5fcbfeaf739b9de4"
VIMEO_SECRET_KEY = "lITFdZdx5ObYOCSTQ80pv/DDt2diSOYURRwB9mJzZoXS2ShP3/3tfuqgzxJS/aCS0hIl307PztjN7vAd3VmBtpMKIbrBeCpIlGyOCRszkZ1t4uR1jHphTo/Of0cgXqd6"

AGORA_APP_ID = "64d0d0ef1715448dae4298949d2bf4a2"
AGORA_APP_CERTIFICATE = "82e3c49f17154c1b86df44d77135b073"

# Custom User Model
AUTH_USER_MODEL = 'authentication.User'

# WSGI_APPLICATION = 'users.wsgi.application'
ASGI_APPLICATION = 'users.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inkster',
        'USER': 'ritesh_db',
        'PASSWORD': 'Rb@12345',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

PICTURE_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'picture')
PICTURE_MEDIA_URL = '/media/picture/'

CORS_ALLOW_ALL_ORIGINS = True

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'bajpaiprabal4@gmail.com'
# EMAIL_HOST_PASSWORD = 'rb@12345'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FROM = 'inksterapp1@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'inksterapp1@gmail.com'
EMAIL_HOST_PASSWORD = 'rb@12345'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_ADMIN = 'inksterapp1@gmail.com'
SENDER_NAME = 'Inkster Team'

# Import Local Settings
# try:
#     from users.settings_local import *
# except ImportError:
#     raise


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': Path(__file__).resolve(strict=True).parent.parent / 'db.sqlite3',
#     }
# }