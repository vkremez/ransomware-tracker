DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = ''
STATIC_URL = '/static/'

import chartkick
STATICFILES_DIRS = (
    chartkick.js(),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '5ry^!i1c6y*$396rb@^ibm1m%eg-aaw8mf0qurk%+a3-r5woo)'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['charts'],
        'APP_DIRS': True,
    },
]

ROOT_URLCONF = 'charts.urls'

WSGI_APPLICATION = 'charts.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'chartkick',
)
ALLOWED_HOSTS = ['*']
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

