#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: Multiprocess.py 
@time: 2017/12/12 18:02 
@describe:多进程案例

"""
import time
import os
from multiprocessing import Pool

def func():
    pass


class Main():
    def __init__(self):
        list1 =[]
        print 'Run the main process (%s).' % (os.getpid())
        mainStart = time.time()  # 记录主进程开始的时间
        pool = Pool(4)  # 开辟4个进程
        for j in list1:
            pool.apply_async(func, args=(j,))  # 函数名，参数
        pool.close()
        pool.join()
        print 'Waiting for all subprocesses done ...'
        print 'All subprocesses done'
        mainEnd = time.time()  # 记录主进程结束时间
        print 'All process ran %0.2f seconds.' % (mainEnd - mainStart)  # 主进程执行时间


if __name__ == "__main__":
    Main() 