from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",
                 default="61qW5-NbXtoIaCvxP_9IBjzXhEof2VznM4aREr1ilL9SL3sefso")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]