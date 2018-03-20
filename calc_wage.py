# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: calc_wage.py 
@time: 2018/03/20 
"""
from datetime import datetime


def calc_wage(user_id,wage,JShuL,JShuH,YangLao,YiLiao,ShiYe,GongShang,ShengYu,GongJiJin):
    # 基数
    ji_shu = wage
    if wage < JShuL:
        ji_shu = JShuL
    if wage > JShuH:
        ji_shu = JShuH

    # 保险
    insurance = ji_shu * (YangLao + YiLiao + ShiYe + GongShang + ShengYu + GongJiJin)

    # 起征点
    threshold = 3500

    # 应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
    taxed_wage = wage - insurance - threshold

    # 全月应纳税额	税率	速算扣除数（元）
    # 不超过 1500 元	3%	0
    # 超过 1500 元至 4500 元	10%	105
    # 超过 4500 元至 9000 元	20%	555
    # 超过 9000 元至 35000 元	25%	1005
    # 超过 35000 元至 55000 元	30%	2755
    # 超过 55000 元至 80000 元	35%	5505
    # 超过 80000 元	45%	13505

    taxes_rate = 0.03
    quick_calculation_deduction = 0

    if taxed_wage <= 1500:
        taxes_rate = 0.03
        quick_calculation_deduction = 0
    elif taxed_wage <= 4500:
        taxes_rate = 0.1
        quick_calculation_deduction = 105
    elif taxed_wage <= 9000:
        taxes_rate = 0.2
        quick_calculation_deduction = 555
    elif taxed_wage <= 35000:
        taxes_rate = 0.25
        quick_calculation_deduction = 1005
    elif taxed_wage <= 55000:
        taxes_rate = 0.3
        quick_calculation_deduction = 2755
    elif taxed_wage < 80000:
        taxes_rate = 0.35
        quick_calculation_deduction = 5505
    else:
        taxes_rate = 0.45
        quick_calculation_deduction = 13505

    # 应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
    tax = taxed_wage * taxes_rate - quick_calculation_deduction

    # 3500一下特殊处理
    if wage <= 3500:
        tax = 0

    # 实际工资
    after_tax_wage = wage - insurance - tax

    # 特殊处理
    if after_tax_wage < 0:
        after_tax_wage = 0
    # 工号, 税前工资, 社保金额, 个税金额, 税后工资
    # print ([job_num, wages, format(insurance,'.2f'), format(taxes_amount,'.2f'), format(real_wages,'.2f')])
    # 增加计算时间
    now = datetime.now()
    time = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")

    return [user_id, int(wage), format(insurance, '.2f'), format(tax, '.2f'), format(after_tax_wage, '.2f'), time]
