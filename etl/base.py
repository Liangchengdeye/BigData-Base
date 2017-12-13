#encoding:utf=8
import os
import sys
reload(sys)
sys.path.append(".")
sys.path.append("..")
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import json
import datetime
import math
import logging


from db.mysql_db import ConnToMysql
from db.mango_db import MongoOperator
from config.conf import *
from logger.logger import Logger
from utils.sendmessage import sendMessage_MSG


def today():
   return  datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')


def now_time():
    return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')


def yesterday():
    return datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(days=1), '%Y-%m-%d')


def conn_to(db, db_server="mysql"):
    if db_server == "mysql":
        return ConnToMysql(db)

    if db_server == "mangodb":
        return MongoOperator(**get_args(db))


def logger(name):
    name = name+".log"
    return Logger(name, logging.WARNING, logging.DEBUG)


def sendMassage_push(content, sendto):
    sendMessage_MSG(content, sendto)


def check_list_set(mylist):
    """
    列表查重
    """
    myset = set(mylist)
    for item in myset:
        if mylist.count(item) > 1:
            print("the %s has found %d" % (item, mylist.count(item)))



if __name__=="__main__":
   conn_to("db")



