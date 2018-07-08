# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
import os

if __name__ == '__main__':
    with os.popen('top -n 1 -b') as fh:
        lines = fh.readlines()
        cpu_line = lines[2]
        mem_line = lines[3]

        cpu_list = cpu_line.split()
        mem_list = mem_line.split()

        cpu = cpu_list[1]
        mem = round(float(int(mem_list[7]) / int(mem_list[3]) * 100), 2)
        print(cpu)
        print(mem)
