#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: Threadpool.py 
@time: 2017/12/12 18:09 
@describe:多线程案例

"""
import time
import threadpool

def func():
    pass


class Main():
    def __init__(self):
        list1 = []
        start_time = time.time()
        # 多线程
        pool = threadpool.ThreadPool(2)
        requests = threadpool.makeRequests(func, list1)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        print '%d second' % (time.time() - start_time)


if __name__ == "__main__":
    Main() 