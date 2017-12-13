#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: test_example.py
@time: 2017/12/2 15:46
@describe: 测试用例

"""
import os
import sys
import json
import datetime
import time
# 导入路径
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
# 导入基础配置信息
from etl.base import *
# 创建log信息
logger = logger("test01-"+today())
conn = conn_to("test01")
conn_test02 = conn_to('test02')
# 抽取（extract）
def select_extract():
    data = []
    sql_data = conn.execute("SELECT * FROM test01")
    print sql_data
    return sql_data


# 转换（transform）清洗-加载（load）至目的端
def clearn_data(data):
    print "I am run"
    values = []
    str_new = data[1][2:4]
    values.append(str_new)
    print str_new
    sql = '''insert into test02 (user_id) values(%s)'''
    conn_test02.insert(sql, [values])


if __name__ == "__main__":

    s_data = select_extract()
    for i_data in s_data:
        clearn_data(i_data)
