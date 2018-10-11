#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from inspection import LoadPattern, DeviceInspector
import os
from os import path
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--src-dir', help='Source dir of log files', type=str, action='store')
parser.add_argument('-o', '--output', help='the report file path', type=str, action='store')
parser.add_argument('-c', '--csv-file', help='The csv file that contains inspection parameters', type=str,
                    action='store')
parser.add_argument('--fn-column', help='the column number which field name is in', type=int, action='store')
parser.add_argument('--re-column', help='the column number which RE-pattern is in', type=int, action='store')
args = parser.parse_args()


print(f" args is {args.csv_file}")
re_f = open(args.csv_file, 'r')


para_dict = LoadPattern(re_f, 1, 3)
para_dict.parse_para()
para = para_dict.get_para()

print(f"para has been parsed\n"+'-'*50)

keys = para.keys()

for key in keys:
    print(f"{key}--->{para[key]}")

print('-'*50)


files = os.listdir(args.src_dir)
logs_path =[]
for file in files:
    if path.isfile(path.join(args.src_dir, file)) and (file[0] != '.'):
        logs_path.append(path.join(args.src_dir, file))
    else:
        continue

report_f = open(args.output, 'w+', newline='')
# csv_writer = csv.writer(report_f)
field_names = ['Hostname', 'MGMT_IP', 'SN', 'Model', 'Software_Verion', 'CPU_Usage', 'MEM_Total', 'MEM_Usage',
               'MEM_Free', 'FAN', 'TEMPERATURE', 'Power']
csv_dict_writer = csv.DictWriter(report_f, field_names)
csv_dict_writer.writeheader()


for log_file in logs_path:
    print(f"file name is {log_file}")
    with open(log_file, 'r') as log_f:
        inspector = DeviceInspector(log_f, para)
        result = inspector.result_gen()
        if result == 1:
            report = inspector.get_report()
        print(report)
        csv_dict_writer.writerow(report)

