from __future__ import absolute_import, unicode_literals
import logging
import time
from threading import Thread, Event

from . import settings, io

logger = logging.getLogger(__name__)

_done_locking_or_unlocking = Event()
_done_locking_or_unlocking.set()


def get_locked():
    # Wait until we have a steady state.
    _done_locking_or_unlocking.wait()
    return io.get_locked()


def get_closed():
    return None


def _unlock():
    _done_locking_or_unlocking.clear()
    io.unlock()
    _done_locking_or_unlocking.set()

    time.sleep(settings.UNLOCK_DURATION)

    _done_locking_or_unlocking.clear()
    io.lock()
    _done_locking_or_unlocking.set()


def unlock(*args, **kwargs):
    # Runs _unlock in separate thread to avoid long response cycles
    unlock_thread = Thread(target=_unlock, args=args, kwargs=kwargs)
    unlock_thread.start()
