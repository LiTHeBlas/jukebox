from __future__ import absolute_import, unicode_literals
import logging

from door import settings, io
from door.api.main import app

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        logger.info('Starting.')
        io.setup()
        logger.debug('GPIO set up.')
        app.run(host='0.0.0.0', debug=settings.DEBUG)
    except (KeyboardInterrupt, SystemExit):
        logger.info('Shutting down.')
        io.cleanup()
