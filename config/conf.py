#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: W_H_J
@license: Apache Licence
@contact: 415900617@qq.com
@site:
@software: PyCharm
@file: conf.py
@time: 2017/12/12 13:22
@describe: 数据库配置文件

"""
import os
from yaml import load
config_path = os.path.join(os.path.dirname(__file__), 'spider.yaml')

with open(config_path) as f:
    cont = f.read()

cf = load(cont)


def get_args(args_name):
    return cf.get(args_name)

