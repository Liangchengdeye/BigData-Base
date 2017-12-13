#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append('.')
import ConfigParser
import pymysql
import decimal
import sys,os,datetime,time
from config.conf import get_args


class ConnToMysql(object):
    
    """
    连接库的初始化
    """
    
    def __init__(self, db):
        self.conn(db)

    def conn(self, db):
        hf = get_args(db)
        hf['charset'] = 'utf8'
        self.conn_to_mysql = pymysql.connect(**hf)
        self.conn_to_mysql.ping(True)
        self.cursor_to_mysql = self.conn_to_mysql.cursor()
        # msyql5.6默认为严格模式，STRICT_TRANS_TABLES，字段超长直接抛异常；
        # 该操作在会话内关闭严格模式，当字段超长时，自动截断，报warning,而不是抛异常。
        self.cursor_to_mysql.execute("set sql_mode='NO_ENGINE_SUBSTITUTION'")

    def execute(self, sql):
        """
        执行sql语句
        """
        self.cursor_to_mysql.execute(sql)
        self.conn_to_mysql.commit()
        return self.cursor_to_mysql.fetchall()
    
    def insert(self, sql, values):
        """
        分批次插入表中的数据
        """
        """
        改变数据格式,将数据由列表转成元组
        """
        values_data = tuple([tuple(i) for i in values])
        max_log_counts = 1000
        for x in xrange(len(values_data) / max_log_counts + 1):
            start = max_log_counts * x
            end = max_log_counts * (x + 1)
            self.cursor_to_mysql.executemany(sql, values_data[start: end])
            self.conn_to_mysql.commit()

    def ones_insert(self, sql, values):
         print "one insert successful"
         values_data = tuple([tuple(i) for i in values])
         self.cursor_to_mysql.executemany(sql, values_data)
         self.conn_to_mysql.commit()

    def insert_sql(self, tableName, data):
        insert_sql_1 = "insert ignore into %s(" % ( tableName )
        insert_sql_2 = "values("
        conn = self.conn_to_mysql
        if isinstance(data, list):
            item = data
        if isinstance(data, dict):
            item = data.keys()
        for k in item:
            v = "%s"
            insert_sql_1 += k + ','
            if isinstance(v, list):
                v = [str(i) for i in v]
                v = ','.join(v)
            elif isinstance(v, int) or isinstance(v, long) or isinstance(v, float) or not v:
                pass
            else:
                v = conn.escape_string(v)
            insert_sql_2 += '%s' %(v) + ','
        insert_sql_1 = insert_sql_1[:-1]+')'
        insert_sql_2 = insert_sql_2[:-1]+')'
        _insert_sql = insert_sql_1 + ' ' + insert_sql_2 + ';'
        return _insert_sql

    def compare_and_insert(self, table, item, data):
        """
        table:表名称
        item：要插入的字段，可以是字典或列表
        data：要批量插入的数据
        """
        sql = self.insert_sql(table, item)
        self.insert(sql, data)

    def create_table(self, table_name, keys, values):
        """
        根据keys 设定表字段，根据values设定字段类型
        """
        print keys
        print values
        create_table_sql_1 = """CREATE TABLE IF NOT EXISTS %s (
            id INT UNSIGNED AUTO_INCREMENT,"""%table_name
        create_table_sql_2 = ""
        for i in range(len(keys)):
            create_table_sql_2 += keys[i] + " "+self.isType(values[i])+","+"\n"
        create_table_sql_3 = """PRIMARY KEY ( id )
            );"""
        create_table_sql = create_table_sql_1+create_table_sql_2+create_table_sql_3
        print create_table_sql
        self.execute(create_table_sql)

    def isType(self, data):
        if isinstance(data, int):
            return "FLOAT" 
        elif isinstance(data, basestring):
            return "VARCHAR(100)"
        elif isinstance(data, decimal.Decimal):
            return "FLOAT" 
        elif isinstance(data, float):
            return "FLOAT" 
        else:
            return "VARCHAR(100)"

    def __del__(self):
        self.conn_to_mysql.commit()
        self.cursor_to_mysql.close()
        self.conn_to_mysql.close()
# test
if __name__=="__main__":
    a = ConnToMysql("test01")
    # data = {}
    # data['a'] = "asdad"
    # data['b'] = 2
    # a.insert_sql("ss",data)
    # a.insert_sql("ss",data)
    # a.compare_and_insert("taster",['foo','baz','z'],[{"sad","2asd","3asd"}])

    # keys=[]
    # vals=[]
    # keys.append('user_id')
    # vals.append('10001')
    # a.create_table('test01', keys, vals)
   
   
    



