# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.core.management import BaseCommand
import json, os, time
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'media', 'notices')
        lists = os.listdir(path)
        for path_name in lists:
            notice = None
            path_notice = os.path.join(path, path_name)
            with open(path_notice, 'rt', encoding='utf-8') as fh:
                notice = json.loads(fh.read())

            self.parse(notice)
            os.unlink(path_notice)

    def parse(self, notice):
        print(notice)
