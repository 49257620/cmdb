# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
from threading import Thread
import logging
import time

logger = logging.getLogger(__name__)


class BaseThread(Thread):
    def __init__(self, type, interval, config):
        super(BaseThread, self).__init__()
        self.daemon = True
        self._type = type
        self._interval = interval
        self._config = config

    def make_event(self):
        return None

    def run(self):
        _type = self._type
        _interval = self._interval
        _config = self._config
        _queue = getattr(_config, 'QUEUE', None)

        logger.info('plugin {0} is running ...'.format(_type))

        while True:

            evt = self.make_event()
            logger.info('evt {0} '.format(evt))
            if evt:
                logger.info('plugin {0} make event'.format(_type))
                _queue.put(evt)

            time.sleep(_interval)
