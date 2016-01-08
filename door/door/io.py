from __future__ import absolute_import, unicode_literals
import logging

import RPi.GPIO as GPIO

from . import settings

logger = logging.getLogger(__name__)


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(settings.LOCK_GPIO_PIN, GPIO.OUT, initial=GPIO.LOW)


def cleanup():
    GPIO.cleanup()


def get_locked():
    return True if GPIO.input(settings.LOCK_GPIO_PIN) == GPIO.LOW else False


def unlock():
    GPIO.output(settings.LOCK_GPIO_PIN, GPIO.HIGH)


def lock():
    GPIO.output(settings.LOCK_GPIO_PIN, GPIO.LOW)
