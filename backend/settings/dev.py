from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5ngm78r0rx)o!5-o(a7ymke-q97@097#k&h)3wae9sat=hh1nx"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
MIDDLEWARE.append("hijack.middleware.HijackUserMiddleware")
INTERNAL_IPS = [
    "127.0.0.1",
]
