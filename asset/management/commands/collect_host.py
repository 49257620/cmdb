# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('test')
