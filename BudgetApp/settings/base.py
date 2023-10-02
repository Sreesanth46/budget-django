from pathlib import Path

import dj_database_url
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config("SECRET_KEY", default="django-insecure$simple.settings.local")

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'BudgetApp.apps.core',
    'BudgetApp.apps.user_management_app',
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "BudgetApp.urls"

INTERNAL_IPS = ["127.0.0.1"]

WSGI_APPLICATION = "BudgetApp.wsgi.application"


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], # [BASE_DIR / "templates"]
        "APP_DIRS": True,
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


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="mysql://root:12345678@localhost:3309/budget"),
    )
}


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

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


# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us")

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_TZ = True


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = "/static/"


# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================
BUDGETAPP_ENVIRONMENT = config("BUDGETAPP_ENVIRONMENT", default="local")

ACCESS_TOKEN_SECRET = config("ACCESS_TOKEN_SECRET", default="ACCESSS_TOKEN_SECRET-DEFAULT")
ACCESS_TOKEN_EXPIRY_MINUTES = config("ACCESS_TOKEN_EXPIRY_MINUTES", default=60)

REFRESH_TOKEN_SECRET = config("REFRESH_TOKEN_SECRET", default="REFRESH_TOKEN_SECRET-DEFAULT")
REFRESH_TOKEN_EXPIRY_HOURS = config("REFRESH_TOKEN_EXPIRY_HOURS", default=1)

MAIL_TOKEN_SECRET = config("MAIL_TOKEN_SECRET", default="MAIL_TOKEN_SECRET-DEFAULT")
MAIL_TOKEN_EXPIRY_MINUTES = config("REFRESH_TOKEN_EXPIRY_HOURS", default=30)
