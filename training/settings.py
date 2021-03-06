"""
Django settings for training project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import sys

import configparser
from django.core.management.color import color_style

# from .logging import LOGGING
style = color_style()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = 'training'
SITE_ID = 40

REVIEWER_SITE_ID = 1

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'training.bhp.org.bw:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'plb+98b-_xium0!e5vk8m+!($)7mu*u3^nos8c3(=!90v2+kx6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ETC_DIR = './etc/'

ALLOWED_HOSTS = ['localhost', 'training.bhp.org.bw', '127.0.0.1']

CONFIG_FILE = f'{APP_NAME}.ini'

CONFIG_PATH = os.path.join(ETC_DIR, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Application definition

NAME = 'training'

INSTALLED_APPS = [
    # 'edc_appointment.apps.AppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'django_countries',
    'django_crypto_fields.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_calendar.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_call_manager.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'training_dashboard.apps.AppConfig',
    # 'training_labs.apps.AppConfig',
    'training_prn.apps.AppConfig',
    'training_subject.apps.AppConfig',
    'training_metadata_rules.apps.AppConfig',
    'training_reference.apps.AppConfig',
    'training_visit_schedule.apps.AppConfig',
    'training.apps.EdcAppointmentAppConfig',
    'training.apps.EdcBaseAppConfig',
    'training.apps.EdcDataManagerAppConfig',
    'training.apps.EdcFacilityAppConfig',
    'training.apps.EdcLocatorAppConfig',
    'training.apps.EdcMetadataAppConfig',
    'training.apps.EdcProtocolAppConfig',
    'training.apps.EdcVisitTrackingAppConfig',
    'training.apps.EdcTimepointAppConfig',
    'training.apps.AppConfig',

]


# AUTO_CREATE_KEYS = True
KEY_PATH = './etc/training/'

BOOTSTRAP3 = {
    'include_jquery': True,
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'training.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'training.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'),
)

TIME_ZONE = 'Africa/Harare'

USE_I18N = True

USE_L10N = False

USE_TZ = True
USE_L10N = False
DATETIME_INPUT_FORMATS = ['%d/%B/%Y %H:%M']
DATE_INPUT_FORMATS = ["%d %B %Y"]
TIME_INPUT_FORMATS = ['%H:%M']
DATETIME_FORMAT = 'd/M/Y H:i'
DATE_FORMAT = 'd/M/Y'
SHORT_DATE_FORMAT = 'd/M/Y'
SHORT_DATETIME_FORMAT = 'd/M/Y H:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'training', 'static')

HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

# dashboards
DASHBOARD_URL_NAMES = {
    'screening_listboard_url': 'training_dashboard:screening_listboard_url',
    'subject_listboard_url': 'training_dashboard:subject_listboard_url',
    'subject_dashboard_url': 'training_dashboard:subject_dashboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'training/base.html',
    'dashboard_base_template': 'training/base.html',
    'subject_dashboard_template': 'training_dashboard/subject/dashboard.html',
    'screening_listboard_template': 'training_dashboard/screening/listboard.html',
    'subject_listboard_template': 'training_dashboard/subject/listboard.html',
}

# edc_facility
COUNTRY = 'botswana'

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''
