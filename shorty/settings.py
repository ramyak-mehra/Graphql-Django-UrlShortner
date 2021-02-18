from decouple import config
from pathlib import Path
import os

# import environ
# from environ import Env, Path
# from decouple import config
# env = Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '%mmqk6xbd25aib2#cv9xi6+ay3yqvvu!3o#oj6&t%!qp03b3o+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'graphene_django',
    'applications',
    'shortener',
    'bulma',
    'django_extensions',
    'notifications',
    'push_notifications',
    'rest_framework',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shorty.urls'

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

WSGI_APPLICATION = 'shorty.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": config("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": config("POSTGRES_USER", "user"),
        "PASSWORD": config("POSTGRES_PASSWORD", ""),
        "HOST": config("SQL_HOST", "localhost"),
        "PORT": config("SQL_PORT", "5432"),
    }
}
PUSH_NOTIFICATIONS_SETTINGS = {

    "USER_MODEL" : "notifications.NotificationUser",
    "FCM_API_KEY" : config("FCM_API_KEY" , "")

}
if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

GRAPHENE = {
    'SCHEMA': 'shorty.schema.schema',
}
SITE_ID = 1
# Captcha System

INSTALLED_APPS += ['captcha', ]
RECAPTCHA_PUBLIC_KEY = os.environ.get(
    "RECAPTCHA_PUBLIC_KEY", default="6LeTp9MZAAAAAFYSpYUXKwlXPeOOoxj1XHRGrWcE")
RECAPTCHA_PRIVATE_KEY = os.environ.get(
    "RECAPTCHA_PRIVATE_KEY", default="6LeTp9MZAAAAAAZpCeXgF95_DZT_t9xJ1glFWSjB")

WEBSITE_NAME = os.environ.get("WEBSITE_NAME", default="vexio.xyz")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL", "")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD", "")

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
# Find templates in the same folder as settings.py.
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)
