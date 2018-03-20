# !usr/bin/env python3
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: calculater.py 
@time: 2018/03/15
"""

# 计算工资

import sys
from multiprocessing import Queue, Process
from config import Config
from calc_wage import calc_wage
from deal_csv import CSV
from deal_command_param import DealCommandParam


def get_user_info(user_file, queue):
    user_csv = CSV(user_file)
    user_data = user_csv.get_data()
    queue.put(user_data)


def calculate_salary(tax_config_file, queue_in, queue_out):
    wage_data = []
    user_data = queue_in.get()

    tax_config = Config(tax_config_file)
    # 所有的城市名
    cities = tax_config.get_sections()
    shot_opts = 'C:c:d:o:'
    comm = DealCommandParam(sys.argv[1:], shot_opts)
    # 配置的城市信息
    city = comm.get_param_by_short_opts('-C')
    city = city.upper()
    if city not in cities:
        city = 'DEFAULT'

    # 具体扣税配置
    JiShuL = tax_config.get_float_value(city, 'JiShuL')
    JiShuH = tax_config.get_float_value(city, 'JiShuH')
    YangLao = tax_config.get_float_value(city, 'YangLao')
    YiLiao = tax_config.get_float_value(city, 'YiLiao')
    ShiYe = tax_config.get_float_value(city, 'ShiYe')
    GongShang = tax_config.get_float_value(city, 'GongShang')
    ShengYu = tax_config.get_float_value(city, 'ShengYu')
    GongJiJin = tax_config.get_float_value(city, 'GongJiJin')

    for user_id, wage in user_data.items():
        # 计算工资
        wage_detail = calc_wage(user_id,wage,JiShuL,JiShuH,YangLao,YiLiao,ShiYe,GongShang,ShengYu,GongJiJin)
        wage_data.append(wage_detail)
    queue_out.put(wage_data)


def save_salary(wage_file, queue):
    salary_data = queue.get()
    user = CSV(wage_file)
    user.write_list_to_file(salary_data)


def print_usage():
    print('[usage] python calculator.py -C chengdu -c test.cfg -d user.csv -o wage.csv')


def main():
    # 处理帮助命令
    if '-h' in sys.argv[1:]:
        print_usage()
        return

    # 取执行参数文件
    shot_opts = 'C:c:d:o:'
    comm = DealCommandParam(sys.argv[1:], shot_opts)
    tax_config_file = comm.get_param_by_short_opts('-c')
    user_file = comm.get_param_by_short_opts('-d')
    wage_file = comm.get_param_by_short_opts('-o')

    queue_to_calc = Queue()
    queue_to_file = Queue()

    Process(target=get_user_info, args=(user_file, queue_to_calc)).start()
    Process(target=calculate_salary, args=(tax_config_file, queue_to_calc, queue_to_file)).start()
    Process(target=save_salary, args=(wage_file, queue_to_file)).start()


if __name__ == '__main__':
    main()
