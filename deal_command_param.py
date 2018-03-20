# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: deal_command_param.py 
@time: 2018/03/20 
"""
import sys
from getopt import getopt


class DealCommandParam(object):
    def __init__(self, params, short_opts):
        self.optlist, self.args = getopt(params, short_opts)

    # 获取短配置参数
    def get_param_by_short_opts(self, index):
        try:
            for opt, param in self.optlist:
                if opt == index:
                    return param
        except getopt.GetoptError as err:
            print(err)
            exit(-1)


# 测试
if __name__ == '__main__':
    comm = DealCommandParam(sys.argv[1:], 'C:c:d:o:')
    result = comm.get_param_by_short_opts('-C')
    print(result)
