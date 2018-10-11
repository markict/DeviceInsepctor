#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import OrderedDict
from collections import namedtuple
from csv import reader
from csv import writer
import re

class DeviceInspector(object):
    log_f = None
    inspect_para = OrderedDict()
    report = OrderedDict()

    def __init__(self,log_f, para_dict):
        self.log_f = log_f
        self.inspect_para = para_dict

    #给定一个文件句柄和一个正则表达式的pattern, 以列表的方式返回匹配结果.
    def para_search(self,file,re_pattern):
        para = []
        for line in file:
            para = re.findall(re_pattern,line.strip())
            if len(para) > 0:
                break


        if len(para) > 0:
            return para
        else:
            return None


    def result_gen(self):
        fields = self.inspect_para.keys()
        for field in fields:
            #每次查完一个pattern必须把文件指针回到文件开始位置
            self.log_f.seek(0)
            result = self.para_search(self.log_f,self.inspect_para[field])
            if result:
                self.report[field] = result[0]
            else:
                self.report[field] = 'N/A'
        return True

    def get_report(self):
        return self.report

class LoadPattern(object):
    csv_f = None
    inspect_para = OrderedDict()
    field_column = 1
    pattern_column = 2

    #传递一个csv文件,里面包含要提取的字段名称和正则pattern, 并标明字段名和pattern的列数
    def __init__(self,csv_f,field_name=1,pattern=2):
        self.csv_f = csv_f
        self.field_column = field_name
        self.pattern_column = pattern
    #对csv中的内容进行解析
    def parse_para(self):
        para_csv = reader(self.csv_f)
        for line in para_csv:
            if line[self.field_column-1] == '':
                continue
            else:
                self.inspect_para[line[self.field_column-1]] = line[self.pattern_column-1]
    #解析结果以OrderedDict形式返回
    def get_para(self):
        return self.inspect_para


