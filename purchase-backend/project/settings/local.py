# Development-specific settings

from .base import INSTALLED_APPS
from decouple import config

DEBUG = True
INSTALLED_APPS_DEV = [
    # Add development-specific apps here
    "apps.supplier_mgmt",
    "apps.order_mgmt",
]

INSTALLED_APPS += INSTALLED_APPS_DEV


# CELERY_BROKER_URL = "amqps://vposmrrw:C3kfYDVd059rPsugtOUCsn89uvCqjMkS@armadillo.rmq.cloudamqp.com/vposmrrw"
CELERY_BROKER_URL = config("rabbitMQ")
CELERY_RESULT_BACKEND = "rpc://"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
