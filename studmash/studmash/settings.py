"""
Django settings for studmash project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qms!-$@aq-u3%11_^_c=p3o+f&i%gtejer@f7ohf-2p+7^p$p('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

VK_APP_ID = '4156636'
VK_API_SECRET = 'wZXxeZIZVOBJMK9OyVVR'

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_SLUGIFY_USERNAMES = True

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/self/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/new-error-url/'

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'social_auth.context_processors.social_auth_by_name_backends',
	'social_auth.context_processors.social_auth_backends',
	'social_auth.context_processors.social_auth_by_type_backends',
	'social_auth.context_processors.social_auth_login_redirect',
)

SOCIAL_AUTH_PIPELINE = (
	'social_auth.backends.pipeline.social.social_auth_user',
	'social_auth.backends.pipeline.associate.associate_by_email',
	'social_auth.backends.pipeline.user.get_username',
	'social_auth.backends.pipeline.user.create_user',
	'social_auth.backends.pipeline.social.associate_user',
	'social_auth.backends.pipeline.social.load_extra_data',
	'social_auth.backends.pipeline.user.update_user_details'
	)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'main'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studmash.urls'

WSGI_APPLICATION = 'studmash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME': 'studmash',
            'USER': 'studmash',
            'PASSWORD': 'qweqweqwe',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
}

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
