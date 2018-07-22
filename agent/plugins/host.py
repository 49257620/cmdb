# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from .base import BaseThread


class Host(BaseThread):

    def __init__(self, queue):
        super(Host, self).__init__('host', 5, queue)

    def make_event(self):
        return {
            'type': self._type,
            'msg': {
                'name': '2222',
                'ip': '2.2.2.2',
                'mac': '',
                'os': '',
                'arch': '',
                'mem': 0,
                'cpu': 0,
                'disk': '{}'
            }
        }
