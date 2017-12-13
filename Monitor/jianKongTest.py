#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: jianKongTest.py 
@time: 2017/12/12 17:44 
@describe:运行结果监控

"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")

import time
# 短信邮箱模块
from utils.sendmessage import *
from utils.sendMails import *
from etl.base import *
logger = logger("test01-"+today())

# 定时任务
def timing():
    while True:
        current_time = time.localtime(time.time())
        if ((current_time.tm_hour == 0) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
            mainStart = time.time()  # 记录主进程开始的时间
            print "start"
            str_msg = play_run()
            baojin(str_msg)
            mainEnd = time.time()  # 记录主进程结束时间
            print 'All Threads ran %0.2f seconds.' % (mainEnd - mainStart)  # 主进程执行时间
        time.sleep(1)

# # 查询现有数据条数
# def chaxun(path):
#     ls = os.listdir(path)
#     count = 0
#     for i in ls:
#         if os.path.isfile(os.path.join(path, i)):
#             count += 1
#     return count
# 查询运行结果数据
def play_run(str_old):
    MSG = "开启查询测试"
    # 发短信模块调用
    sendMessage_MSG(MSG, '1850014----,')
    # 发邮箱模块
    reciever = ['415900617@qq.cn']
    subject = '邮件标题'
    sendmail(MSG, reciever, subject)
    return MSG

# 报警处理
def baojin(MSG):
    MSG ="【警报】"
    # 发送警报短信
    sendMessage_MSG(MSG, '1850014----,')
    logger.error(MSG)

class Main():
    def __init__(self):
        # 开启定时任务
        timing()



if __name__ == "__main__":
    Main()
    a = raw_input()
