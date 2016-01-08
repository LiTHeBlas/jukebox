from __future__ import absolute_import, unicode_literals
import logging
from os import environ

logger = logging.getLogger(__name__)


DEBUG = environ.get('DEBUG', False)
SECRET_KEY = environ['SECRET_KEY']
ALLOWED_IPS = environ.get('ALLOWED_IPS', '').split(',')

LOCK_GPIO_PIN = int(environ['LOCK_GPIO_PIN'])
UNLOCK_DURATION = int(environ.get('UNLOCK_DURATION', '10'))
