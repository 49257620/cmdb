# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.core.management import BaseCommand
import json, os, datetime
from django.conf import settings
from webanalysis.models import AccessLog


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'media', 'notices')
        lists = os.listdir(path)
        for path_name in lists:
            notice = None
            path_notice = os.path.join(path, path_name)
            with open(path_notice, 'rt', encoding='utf-8') as fh:
                notice = json.loads(fh.read())

            try:
                self.parse_notice(notice)
            except BaseException as e:
                print(e)
            os.unlink(path_notice)

    def parse_notice(self, notice):
        with open(notice['path'], 'rt', encoding='utf-8') as fh:
            for line in fh.readlines():
                line_info = line.split()
                ptime = datetime.datetime.strptime(line_info[3], "[%d/%b/%Y:%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                # print(notice['file_id'], line_info[0], line_info[6], line_info[8],ptime)
                log = AccessLog(file_id=notice['file_id'], ip=line_info[0], url=line_info[6], status_code=line_info[8],
                                access_time=ptime)
                log.save()

            print('parse over :', notice['file_id'])
