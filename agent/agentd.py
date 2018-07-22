# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

import argparse
import logging
import os
from gconfig import Config
from queue import Queue
from plugins.host import Host
from plugins.ens import  ENS
import time

logger = logging.getLogger(__name__)


def main(config):
    ths = []
    ths.append(ENS(config))
    ths.append(Host(config))

    for th in ths:
        th.start()

    while True:
        time.sleep(3)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='server host')
    parser.add_argument('-P', '--port', type=int, default=8888, help='server port')
    parser.add_argument('-V', '--verbose', action='store_true', help='debug mod')

    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    pid = os.getpid()
    fmt = '%(asctime)s - %(name)s - %(levelname)s:%(message)s'
    level = logging.DEBUG if args.verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format=fmt,
        filemode='w',
        filename=os.path.join(base_dir, 'logs', 'agentd.log')
    )

    logger.info('agent start: {0}'.format(pid))
    logger.debug('debug msg')

    config = Config

    setattr(config, 'SERVER', '{0}:{1}'.format(args.host, args.port))
    setattr(config, 'PID', pid)
    setattr(config, 'QUEUE', Queue())

    main(config)
