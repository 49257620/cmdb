# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from threading import Thread
import logging
import time
from queue import Queue
from queue import Empty

logger = logging.getLogger(__name__)


class ENS(Thread):
    def __init__(self, config):
        super(ENS, self).__init__()
        self._config = config

    def run(self):
        _queue = getattr(self._config, 'QUEUE', None)

        while True:
            try:
                evt = _queue.get(block=True, timeout=3)
                logger.info('ENS get event:{}'.format(evt))
            except Empty as e:
                time.sleep(3)
