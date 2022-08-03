'''
This file contains all the settings used in production.
'''

from server.settings.components import config



DEBUG = False
ALLOWED_HOSTS = ('.{}'.format(config('DOMAIN_NAME')),)
STATIC_ROOT = '/var/www/django/static'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
MEDIA_ROOT = '/var/www/django/media'

# Password validation
_PASS = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = (
    {'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS)},
    {'NAME': '{0}.MinimumLengthValidator'.format(_PASS)},
    {'NAME': '{0}.CommonPasswordValidator'.format(_PASS)},
    {'NAME': '{0}.NumericPasswordValidator'.format(_PASS)},
)

# Security
SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
