"""
Django settings for wed project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aeyo5d9h8u=t7_3rj7&6o6ev_cqgmkdw9xs2ys0ly7+ugja&=k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'wedd.apps.WeddConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wed.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'wed.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# import urllib.parse

# # Replace 'your_username' and 'your_password' with your actual MongoDB Atlas credentials
# username = 'wandekar'
# password = 'gima@142'

# # Encode the username and password
# encoded_username = urllib.parse.quote_plus(username)
# encoded_password = urllib.parse.quote_plus(password)

# # Use the encoded username and password in your MongoDB connection URI
# connection_uri = f'mongodb+srv://{encoded_username}:{encoded_password}@your_cluster_host/dbname'

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'wandekar',
#         'CLIENT': {
#             'host': 'connection_uri',
#             'username': 'wandekar',
#             'password': 'gima@142',
#             'authSource': 'admin',
#             'authMechanism': 'SCRAM-SHA-1',
#         }
#     }
# }

# RENDER LIVE DATABSE

import dj_database_url

DATABASES = {
    'default' : dj_database_url.parse('postgres://wandekar:gryCjo3DEbe3uQkpKWDypXfF3jsNHj7a@dpg-cmginu0cmk4c73er2190-a.oregon-postgres.render.com/wandekar_u7za')
 
}
# settings.py

# Email configuration using Gmail SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'wandekarkunbi@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'gima@142'  # Your Gmail password
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'wandekarkunbi@gmail.com'  # Your Gmail email address (same as EMAIL_HOST_USER)


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# STATIC_URL = 'static/'

# STATICFILES_DIRS=[
#     os.path.join(BASE_DIR,"static")
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
