# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: config.py 
@time: 2018/03/20 
"""

# config = configparser.RawConfigParser()
#     config.read(file_path)
#     # 获取所有的section
#     sections = config.sections()
#     if city not in sections:
#         city = 'DEFAULT'
#
#     JiShuL = config.getfloat(city, 'JiShuL')
#     JiShuH = config.getfloat(city, 'JiShuH')
#     YangLao = config.getfloat(city, 'YangLao')
#     YiLiao = config.getfloat(city, 'YiLiao')
#     ShiYe = config.getfloat(city, 'ShiYe')
#     GongShang = config.getfloat(city, 'GongShang')
#     ShengYu = config.getfloat(city, 'ShengYu')
#     GongJiJin = config.getfloat(city, 'GongJiJin')

import configparser
import sys


class Config(object):

    # 初始化解析器
    def __init__(self, value):
        self.config_path = value
        self.config_parser = configparser.RawConfigParser()
        self.config_parser.read(self.config_path)

    # 取浮点数
    def get_float_value(self, section, index):
        return self.config_parser.getfloat(section, index)

    # 获取sections
    def get_sections(self):
        return self.config_parser.sections()


# 测试
if __name__ == '__main__':
    config_path = sys.argv[1]
    config = Config(config_path)
    result = config.get_float_value('DEFAULT', 'JiShuL')
    print(result)




