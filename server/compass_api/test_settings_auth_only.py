from .settings import *

# Isolate URL resolution for auth tests to avoid unrelated app import errors.
ROOT_URLCONF = 'auth_app.urls'
