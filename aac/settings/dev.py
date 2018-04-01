from aac.settings.base import *

# Use this secret in development environment only!
SECRET_KEY = "d-z-_k2*kg%8&h57jn10s+6!j)@_2wvhzswn%#b3d590$72idq"

# Debug options.
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Extended application definition.
INSTALLED_APPS += [
    "django_extensions",
]

# Sets default response format for tests.
REST_FRAMEWORK["TEST_REQUEST_DEFAULT_FORMAT"] = "json"
# Databases.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(TMP_DIR, "db.sqlite3"),
    }
}
