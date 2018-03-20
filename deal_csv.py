# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: deal_csv.py 
@time: 2018/03/20 
"""
import csv


class CSV(object):
    def __init__(self, value):
        self.file_path = value

    def get_data(self):
        try:
            result = {}
            with open(self.file_path, 'r') as file:
                file_content = csv.reader(file)
                for line in file_content:
                    result[line[0]] = float(line[-1])
            return result
        except:
            print('need config file')
            exit(-1)


    def write_list_to_file(self, data):
        try:
            with open(self.file_path, 'a', newline="") as file:
                writer = csv.writer(file, dialect="excel")
                writer.writerows(data)
        except:
            print('file not exist')
            exit(-1)