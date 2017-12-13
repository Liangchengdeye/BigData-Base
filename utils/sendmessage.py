#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 发送短信模块
import urllib2
   
def sendingMessage(phone, massages, phonenumber):
    # 短信接口
    chuanglanBaseUrl=" URL "
    chuanglanUn="JI0327"
    chuanglanPw="158572"        
    print chuanglanBaseUrl % (chuanglanUn, chuanglanPw, phone, massages, phonenumber)
    req = urllib2.Request(chuanglanBaseUrl % (chuanglanUn, chuanglanPw, phone, massages, phonenumber))
    res_data = urllib2.urlopen(req)
    res = res_data.read()
#        print res


def sendMessage_MSG(content, numbers):
        
        sendingMessage(numbers, content, len(numbers.split(',')))
        
# test
if __name__=='__main__':
    # 调用短信模块
    content = "我是测试短信"
    sendMessage_MSG(content, '18338888888,')
