from mysite.settings import *






# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ohmt&)96o(s4$b$0o@)zg2im2$gie9z7b5=@%%k$4ggl=+#!kw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# install_apps = []

# sitest frameworks
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_ROOT= BASE_DIR/'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
