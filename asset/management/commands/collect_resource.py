# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.core.management import BaseCommand
import json
import shutil
import os
from django.conf import settings
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C

from asset.models import Resource


class Command(BaseCommand):
    def handle(self, *args, **options):
        Options = namedtuple('Options',
                             ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                              'diff'])
        options = Options(connection='smart', module_path=[], forks=10, become=None, become_method=None,
                          become_user=None,
                          check=False, diff=False)

        loader = DataLoader()
        passwords = {}

        results_callback = ResultCallback()

        inventory = InventoryManager(loader=loader, sources=os.path.join(settings.BASE_DIR, 'etc', 'hosts'))  # 剧本的位置

        variable_manager = VariableManager(loader=loader, inventory=inventory)

        dest_path = '/tmp/resources.py'
        # ansible all -i etc/hosts -m setup
        play_source = {
            'name': "CMDB Collect",
            'hosts': 'all',  # 在哪些主机上执行
            'gather_facts': 'no',
            'tasks': [  # 执行的任务列表
                {
                    'name': 'collect_server_info',  # 任务名称
                    'setup': ''  # 执行任务模块
                },
                {
                    'name': 'copy_file',  # 任务名称
                    'copy': 'src='+os.path.join(settings.BASE_DIR, 'etc', 'resources.py')+' dest='+dest_path  # 执行任务模块
                },
                {
                    'name': 'collect_resource',  # 任务名称
                    'command': 'python3 '+ dest_path # 执行任务模块
                }
            ]
        }

        play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

        tqm = None
        try:
            tqm = TaskQueueManager(
                inventory=inventory,
                variable_manager=variable_manager,
                loader=loader,
                options=options,
                passwords=passwords,
                stdout_callback=results_callback,
            )
            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()

            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


class ResultCallback(CallbackBase):
    def __init__(self):
        self._cache_host = {}
        super(ResultCallback, self).__init__()

    def v2_runner_on_ok(self, result, **kwargs):
        if result.task_name == 'collect_server_info':
            facts = result._result.get('ansible_facts', {})
            ip = facts.get('ansible_default_ipv4', {}).get('address', '')
            self._cache_host[result._host.name] = ip
        elif result.task_name == 'copy_file':
            pass
        elif result.task_name == 'collect_resource':
            ip = self._cache_host.get(result._host.name)
            resource = result._result.get('stdout_lines',[])
            record = Resource()
            record.ip = ip
            record.cpu = resource[0]
            record.mem = resource[1]
            record.save()

